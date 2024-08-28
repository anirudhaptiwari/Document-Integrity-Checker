from flask import Flask, request, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import hashlib
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  

# PostgreSQL configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:user@localhost/Test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for file hashes
class FileHash(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    unique_name = db.Column(db.String(100), unique=True, nullable=False)
    hash_value = db.Column(db.String(64), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<FileHash {self.unique_name}>'

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        session['action'] = request.form['action']
        if session['action'] == 'generate':
            return redirect(url_for('upload_file'))
        elif session['action'] == 'check':
            return redirect(url_for('check_integrity'))
    return render_template('home.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        unique_name = request.form['unique_name']
        if file and unique_name:
            os.makedirs('uploads', exist_ok=True)
            file_path = os.path.join('uploads', file.filename)
            file.save(file_path)
            calculated_hash = calculate_file_hash(file_path)
            
            # Save hash to database
            new_hash = FileHash(unique_name=unique_name, hash_value=calculated_hash)
            db.session.add(new_hash)
            db.session.commit()
            
            return render_template('upload.html', calculated_hash=calculated_hash)
    return render_template('upload.html')

@app.route('/check_integrity', methods=['GET', 'POST'])
def check_integrity():
    error = None
    is_intact = None
    if request.method == 'POST':
        file = request.files['file']
        unique_name = request.form.get('unique_name')
        hash_value = request.form.get('hash_value')
        if file and (unique_name or hash_value):
            file_path = os.path.join('uploads', file.filename)
            file.save(file_path)
            
            if unique_name:
                stored_hash = FileHash.query.filter_by(unique_name=unique_name).first()
                if stored_hash:
                    stored_hash = stored_hash.hash_value
                else:
                    error = 'Unique name not found'
            else:
                stored_hash = hash_value
            
            if stored_hash:
                is_intact = check_file_integrity(file_path, stored_hash)
            else:
                error = 'Invalid unique name or hash value. Please try again.'
    return render_template('check_integrity.html', error=error, is_intact=is_intact)

def calculate_file_hash(file_path):
    """
    Calculates the hash of a file using a strong hashing algorithm.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The calculated hash value in hexadecimal format.
    """
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return None

    try:
        with open(file_path, 'rb') as f:
            hasher = hashlib.sha256()
            chunk_size = 65536
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                hasher.update(chunk)
            calculated_hash = hasher.hexdigest()
    except IOError as e:
        print(f"Error reading file: {e}")
        return None

    return calculated_hash

def check_file_integrity(file_path, stored_hash):
    """
    Checks the integrity of a file by comparing its calculated hash with a stored hash.

    Args:
        file_path (str): The path to the file.
        stored_hash (str): The pre-calculated hash of the original file.

    Returns:
        bool: True if the hashes match, False otherwise.
    """
    calculated_hash = calculate_file_hash(file_path)
    if calculated_hash is None:
        return False

    if calculated_hash == stored_hash:
        print("The Document is intact.")
        return True
    else:
        print("The Document has been modified.")
        return False

if __name__ == '__main__':
    app.run(debug=True)
