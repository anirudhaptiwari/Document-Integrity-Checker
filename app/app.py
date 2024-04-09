from flask import Flask, request, render_template, redirect, url_for, session
import hashlib
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  

# Store the hashes in a dictionary for simplicity
hashes = {}

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
            # Ensure the uploads directory exists
            os.makedirs('uploads', exist_ok=True)
            file_path = os.path.join('uploads', file.filename)
            file.save(file_path)
            calculated_hash = calculate_pdf_hash(file_path)
            # Save the hash with a unique name
            hashes[unique_name] = calculated_hash
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
        if file and (unique_name in hashes or hash_value):
            file_path = os.path.join('uploads', file.filename)
            file.save(file_path)
            stored_hash = hashes.get(unique_name) if unique_name else hash_value
            is_intact = check_pdf_integrity(file_path, stored_hash)
        else:
            error = 'Invalid unique name or hash value. Please try again.'
    return render_template('check_integrity.html', error=error, is_intact=is_intact)

def calculate_pdf_hash(file_path):
  """
  Calculates the hash of a PDF document using a strong hashing algorithm.

  Args:
      file_path (str): The path to the PDF file.

  Returns:
      str: The calculated hash value in hexadecimal format.
  """

  if not os.path.exists(file_path):
    print(f"Error: File '{file_path}' not found.")
    return None

  try:
    with open(file_path, 'rb') as f:
      # Use a strong hashing algorithm like SHA-256
      hasher = hashlib.sha256()
      # Read the PDF in chunks for efficiency
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


def check_pdf_integrity(file_path, stored_hash):
  """
  Checks the integrity of a PDF document by comparing its calculated hash with a stored hash.

  Args:
      file_path (str): The path to the PDF file.
      stored_hash (str): The pre-calculated hash of the original PDF.

  Returns:
      bool: True if the hashes match, False otherwise.
  """

  if not os.path.exists(file_path):
    print(f"Error: File '{file_path}' not found.")
    return False

  try:
    with open(file_path, 'rb') as f:
      # Use a strong hashing algorithm like SHA-256
      hasher = hashlib.sha256()
      # Read the PDF in chunks for efficiency
      chunk_size = 65536
      while True:
        chunk = f.read(chunk_size)
        if not chunk:
          break
        hasher.update(chunk)
      calculated_hash = hasher.hexdigest()
  except IOError as e:
    print(f"Error reading file: {e}")
    return False

  if calculated_hash == stored_hash:
    print("The Document is intact.")
    return True
  else:
    print("The Document has been modified.")
    return False


if __name__ == '__main__':
    app.run(debug=True)
