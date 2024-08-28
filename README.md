# Document Integrity Checker

## Description
This Flask-based web application allows users to check the integrity of any document. It uses the SHA-256 hashing algorithm to calculate a unique hash for each uploaded document. Later, it can compare the calculated hash of the document with the stored hash to check if the document has been modified.

## Features
- User Authentication
- File Upload
- Hash Generation
- Integrity Check

## Technologies Used
- Python
- Flask
- hashlib
- os
- HTML
- CSS
- JavaScript

## Installation

1. **Clone the repository**: Clone this repository to your local machine using the command:
```bash
git clone https://github.com/anirudhaptiwari/Document-Integrity-Checker.git
```

2. **Navigate to the project directory**:Use the command:
```bash
cd Document-Integrity-Checker
```
<!--3. **Create a virtual environment**: It’s a good practice to create a virtual environment for your Python projects use:
```bash
python3 -m venv env
```
4.**Activate the virtual environment**: The command to activate the virtual environment depends on your operating system:

**On Windows use**
```bash
.\env\Scripts\activate
```
**On Unix or MacOS use**
```bash
source env/bin/activate 
```                     -->
3.**Install the dependencies**: The project requires Flask and its dependencies. You can install them using pip:
```bash
pip install flask
```
## Usage

1. **Run the application**: You can run the application using the command:
```bash
python app.py
```
This will start the Flask development server.

2. **Access the application**: Open web browser and navigate to
```bash
http://localhost:5000
```
This will take you to the login page of the application.

4. **Use the application**: From the login page, you can log in to the application **(the default username and password are both ‘admin’)** Once logged in, you can choose to either generate a hash for a new document or check the integrity of an existing document.


## Contribution

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.


