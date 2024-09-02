# EPC Data Import

## Overview

This project provides a script to import Energy Performance Certificate (EPC) data from multiple CSV files into an SQLite database. The script processes large datasets efficiently, handling them in chunks, and includes logging for monitoring the import process.

## Requirements

- Python 3.7+
- Pandas
- SQLAlchemy

## How to Run

1. **Clone the Repository** (if applicable):

   ```bash
   cd epc-import
   ```
2. **Install the Dependencies:**

Use pip to install the required Python packages:

```bash
pip install pandas sqlalchemy
```

3. **Prepare the Data:**

Ensure that the certificates.csv files are present in the project directory. The script will process all certificates.csv files in the directory.

The CSV files should have the following columns:

LMK_KEY
LODGEMENT_DATE
TRANSACTION_TYPE
TOTAL_FLOOR_AREA
ADDRESS
POSTCODE

4. **Run the Data Import Script:**

Execute the script to start importing the data into the database:

```bash
python epc_import.py
```

This will begin reading each CSV file in chunks and inserting the data into an SQLite database (epc_data.db) located in the same directory. The script will process all certificates.csv files in the directory.

5. **Check the Logs:**

After the script runs, you can check the epc_import.log file in the same directory for details on the import process, including any errors encountered.





