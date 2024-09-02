import pandas as pd
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
import logging
import os

# Set up logging - handy for checking how things went
logging.basicConfig(
    filename='epc_import.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)

# Database setup - I'm just using SQLite here, but this could be swapped out for something else
DATABASE_URI = 'sqlite:///epc_data.db'
engine = create_engine(DATABASE_URI)
metadata = MetaData()

# Define the EPC table schema
epc_table = Table(
    'epc_data', metadata,
    Column('LMK_KEY', String, primary_key=True),
    Column('LODGEMENT_DATE', String),
    Column('TRANSACTION_TYPE', String),
    Column('TOTAL_FLOOR_AREA', Integer),
    Column('ADDRESS', String),
    Column('POSTCODE', String)
)

# Create the table if it doesn't exist already
metadata.create_all(engine)

def process_chunk(chunk, connection):
    """Insert a chunk of data into the database"""
    try:
        chunk.to_sql('epc_data', con=connection, if_exists='append', index=False)
        logging.info(f'Processed chunk with {len(chunk)} records')
    except Exception as e:
        logging.error(f'Error processing chunk: {e}')

def import_epc_data(directory_path, chunksize=10000):
    """Loop through all CSV files in the directory and import the data"""
    connection = engine.connect()

    # Go through each file in the directory
    for file_name in os.listdir(directory_path):
        if file_name.endswith('.csv'):
            file_path = os.path.join(directory_path, file_name)
            try:
                logging.info(f'Starting import from {file_path}')
                
                # Read and process the data in chunks to handle large files
                for chunk in pd.read_csv(file_path, usecols=[
                        'LMK_KEY', 'LODGEMENT_DATE', 'TRANSACTION_TYPE',
                        'TOTAL_FLOOR_AREA', 'ADDRESS', 'POSTCODE'],
                        chunksize=chunksize
                    ):
                    process_chunk(chunk, connection)

                logging.info(f'Successfully imported {file_name}')
            except Exception as e:
                logging.error(f'Error during import from {file_path}: {e}')

    connection.close()

if __name__ == '__main__':
    # Use current directory, where CSV files are located
    import_epc_data('.')
