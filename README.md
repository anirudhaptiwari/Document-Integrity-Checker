# Document Integrity Checker

## Description
This project provides a simple way to check the integrity of any document. It uses SHA-256 hashing algorithm to calculate the hash of the original document and then compares it with the hash of the document at any later point. If the hashes match, the document is deemed intact; if they don't, the document has been modified.

## Technologies Used
- Python
- hashlib
- os

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

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


