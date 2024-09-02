import unittest
from corporate_land_ownership import load_company_relations, load_land_ownership, get_total_land

class TestCorporateLandOwnership(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
        self.company_relations = {
            "R764915829891": ["C100517359149"],
            "C622523283889": ["C104936104"]
        }
        self.land_ownership = {
            "R764915829891": ["T100018863440"],
            "C100517359149": ["T100030485625", "T100073722185"],
            "C104936104": ["T100075985035"]
        }

    def test_single_company_ownership(self):
        total_land = get_total_land("R764915829891", self.company_relations, self.land_ownership)
        self.assertEqual(total_land, 3)

    def test_multiple_company_ownership(self):
        total_land = get_total_land("C622523283889", self.company_relations, self.land_ownership)
        self.assertEqual(total_land, 1)

    def test_company_with_no_land(self):
        total_land = get_total_land("NonExistentCompany", self.company_relations, self.land_ownership)
        self.assertEqual(total_land, 0)

    def test_company_with_no_subsidiaries(self):
        total_land = get_total_land("C104936104", self.company_relations, self.land_ownership)
        self.assertEqual(total_land, 1)

if __name__ == "__main__":
    unittest.main()
