import re

def extract_urls_from_text_file(file_path, encoding='utf-8'):
    urls = []
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    
    try:
        with open(file_path, 'r', encoding=encoding, errors='replace') as file:
            text = file.read()
            urls = re.findall(url_pattern, text)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except UnicodeDecodeError:
        print(f"Error decoding the file using {encoding} encoding.")
    
    return urls

# Example usage
file_path = 'train.txt'
extracted_urls = extract_urls_from_text_file(file_path)

if extracted_urls:
    print("Extracted URLs:")
    for url in extracted_urls:
        print(url)
else:
    print("No URLs were extracted from the file.")
