import re
import json

def parse_extracted_text(text):
    """Parse extracted text into structured data."""
    data = {
        "Patient Name": re.search(r"Patient\s*Name:\s*(.*)", text, re.IGNORECASE).group(1).strip() if re.search(r"Patient\s*Name:\s*(.*)", text, re.IGNORECASE) else "Unknown",
        "Date of Birth": re.search(r"Date\s*of\s*Birth:\s*(.*)", text, re.IGNORECASE).group(1).strip() if re.search(r"Date\s*of\s*Birth:\s*(.*)", text, re.IGNORECASE) else "Unknown",
        "Assessment Date": re.search(r"Assessment\s*Date:\s*(.*)", text, re.IGNORECASE).group(1).strip() if re.search(r"Assessment\s*Date:\s*(.*)", text, re.IGNORECASE) else "Unknown",
        "Diagnosis": re.search(r"Diagnosis:\s*(.*)", text, re.IGNORECASE).group(1).strip() if re.search(r"Diagnosis:\s*(.*)", text, re.IGNORECASE) else "Unknown"
    }
    return data

def save_to_json(data, output_file):
    """Save structured data to a JSON file."""
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)
