# Land Parcels

## Overview

This Python script identifies parcels of land from a list of x,y coordinates and calculates the perimeter of each parcel. The script can handle complex shapes and ensures accurate perimeter calculations.

## Requirements

- Python 3.7+

## How to Run

1. Run the script:
   ```bash
   python land_parcels.py
  ```

2. Customize the input points list in land_parcels.py to test different sets of coordinates.

## Testing

Run the unit tests to verify the functionality:
```bash
python -m unittest test_compute_parcels.py
```

## Project Structure

land_parcels.py: Contains the core logic to compute the number of parcels and their perimeters.
test_land_parcels.py: Unit tests to ensure the correctness of the land parcels logic.

## Notes

The algorithm uses a Breadth-First Search (BFS) approach to identify connected parcels and calculate perimeters.
The solution is optimized for readability and correctness.