import hashlib
import os

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

# Example usage (replace with your actual file path)
file_path = (r"C:\Users\Anirudha\Downloads\arr.pdf") 

stored_hash = calculate_pdf_hash(file_path)

if stored_hash:
  print("Calculated hash:", stored_hash)
  # Store this hash value securely for future integrity checks
else:
  print("Error generating hash.")
