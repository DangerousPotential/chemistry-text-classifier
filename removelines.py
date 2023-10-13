import re

def remove_lines_with_pattern(file_path, pattern, encoding='utf-8'):
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return
    
    # Filter out lines that match the pattern
    filtered_lines = [line.strip() for line in lines if not re.match(pattern, line)]

    return filtered_lines

def save_lines_to_file(lines, output_file):
    try:
        with open(output_file, 'w') as file:
            for line in lines:
                file.write(line + '\n')
        print(f"Processed lines saved to {output_file}")
    except IOError:
        print(f"Error: Could not write to the file {output_file}")

# Example usage
file_path = 'extracted_url.txt'
output_file = 'processed_text.txt'

# Define the pattern to match the specified URLs
pattern = r'^https://socratic\.org/questions/\d+'

filtered_lines = remove_lines_with_pattern(file_path, pattern)

if filtered_lines:
    save_lines_to_file(filtered_lines, output_file)
else:
    print("No lines were removed.")
