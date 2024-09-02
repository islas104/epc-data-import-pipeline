import unittest
from compute_parcels import computeParcelPerimeters

class TestComputeParcelPerimeters(unittest.TestCase):

    def test_single_square(self):
        points = ["0,0"]
        result = computeParcelPerimeters(points)
        self.assertEqual(result, [4])

    def test_line_parcel(self):
        points = ["0,0", "0,1", "0,2"]
        result = computeParcelPerimeters(points)
        self.assertEqual(result, [8])

    def test_disconnected_parcels(self):
        points = ["0,0", "0,1", "0,2", "2,0"]
        result = computeParcelPerimeters(points)
        self.assertEqual(result, [8, 4])

    def test_complex_parcel(self):
        points = ["1,1", "1,2", "2,1", "2,2"]
        result = computeParcelPerimeters(points)
        self.assertEqual(result, [8])

    def test_no_parcel(self):
        points = []
        result = computeParcelPerimeters(points)
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()
