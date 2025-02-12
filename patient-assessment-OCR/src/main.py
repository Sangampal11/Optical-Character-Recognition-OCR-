import argparse
from Extrected_OCR import extract_text
from parse_data import parse_extracted_text, save_to_json
from databse_op import create_database, insert_data


def main():
    parser = argparse.ArgumentParser(description="Process patient assessment forms.")
    parser.add_argument("--input", required=True, help="Path to the input file (JPEG/PDF).")
    parser.add_argument("--output", required=True, help="Path to save the JSON output.")
    parser.add_argument("--db", required=True, help="Path to the SQLite database.")
    args = parser.parse_args()

    # Step 1: Extract text
    text = extract_text(args.input)

    # Step 2: Parse text
    data = parse_extracted_text(text)
    save_to_json(data, args.output)

    # Step 3: Store in database
    create_database(args.db)
    insert_data(args.db, data)

if __name__ == "__main__":
    main()