import sqlite3

def create_database(db_name):
    """Create a SQLite database and table."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patient_assessments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_name TEXT NOT NULL,
            date_of_birth TEXT NOT NULL,
            assessment_date TEXT NOT NULL,
            diagnosis TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_data(db_name, data):
    """Insert structured data into the database."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO patient_assessments (patient_name, date_of_birth, assessment_date, diagnosis)
        VALUES (?, ?, ?, ?)
    ''', (data["Patient Name"], data["Date of Birth"], data["Assessment Date"], data["Diagnosis"]))
    conn.commit()
    conn.close()