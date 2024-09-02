# Corporate Land Ownership

## Overview

This Python script calculates the total land owned by a company, including both direct and indirect ownership through its subsidiaries. The data is read from CSV files and processed in-memory for quick calculations.

## Requirements

- Python 3.7+

## How to Run

1. Ensure the `company_relations.csv` and `land_ownership.csv` files are in the same directory as the script.

2. Run the script:
   ```bash
   python corporate_land_ownership.py
   ```

3. Customize the company_id in corporate_land_ownership.py to check land ownership for different companies.

## Testing

Run the unit tests to validate the logic:
```bash
python -m unittest test_corporate_land_ownership.py
```

## Project Structure 

corporate_land_ownership.py: Core logic for calculating land ownership, both direct and indirect.
test_corporate_land_ownership.py: Unit tests for the corporate land ownership logic.

## Notes

The script efficiently handles the hierarchy of companies using recursion.
It can be easily extended to handle larger datasets or more complex ownership structures.