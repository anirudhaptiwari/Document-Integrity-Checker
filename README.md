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

## Installation and Usage
1. Clone this repository to your local machine.
2. Navigate to the directory containing the script.
3. Run the script using Python.

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


