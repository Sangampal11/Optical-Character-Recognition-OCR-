import re
import json

def parse_extracted_text(text):
    """Parse extracted text into structured data."""
    data = {
        "Patient Name": re.search(r"Patient Name:\s*(.*)", text).group(1).strip(),
        "Date of Birth": re.search(r"Date of Birth:\s*(.*)", text).group(1).strip(),
        "Assessment Date": re.search(r"Assessment Date:\s*(.*)", text).group(1).strip(),
        "Diagnosis": re.search(r"Diagnosis:\s*(.*)", text).group(1).strip()
    }
    return data

def save_to_json(data, output_file):
    """Save structured data to a JSON file."""
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)