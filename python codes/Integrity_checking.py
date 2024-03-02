import hashlib
import os

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

# Example usage (replace with your actual file path and hash)
file_path = (r"C:\Users\Anirudha\Downloads\test.jpg")
stored_hash = "a39c4520131dd8feee818889cd57ef47af6ec4cfa76e8c98c619c408fc09c684"

check_pdf_integrity(file_path, stored_hash)
