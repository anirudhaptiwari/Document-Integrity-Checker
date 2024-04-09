# Document Integrity Checker

## Description
This Flask-based web application allows users to check the integrity of any PDF document. It uses the SHA-256 hashing algorithm to calculate a unique hash for each uploaded document. Later, it can compare the calculated hash of the document with the stored hash to check if the document has been modified.

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

2. **Navigate to the directory containing the script**: Use the command:
   ```bash
   cd <project_directory>
   ```
3. **Create a virtual environment**: It’s a good practice to create a virtual environment for your Python projects. You can do this using the venv module:
   ```bash
   python3 -m venv env
   ```
4.**Activate the virtual environment**: The command to activate the virtual environment depends on your operating system:
```bash
On Windows, use: .\env\Scripts\activate
On Unix or MacOS, use: source env/bin/activate
```
5.**Install the dependencies**: The project requires Flask and its dependencies. You can install them using pip:
```bash
pip install flask
```

```python
# Example usage (replace with your actual file path)
file_path = (r"C:\Users\Anirudha\Downloads\test.jpg") 

# Calculate and store the hash of the original document
stored_hash = calculate_pdf_hash(file_path)

if stored_hash:
  print("Calculated hash:", stored_hash)
  # We need to store this hash value securely for future integrity checks
else:
  print("Error generating hash.")

# Check the integrity of the document at a later point
check_pdf_integrity(file_path, stored_hash)
```

## Contribution

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.


