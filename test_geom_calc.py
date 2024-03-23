import unittest
from geom_calc import area_of_circle, area_of_triangle

class TestGeometryCalculations(unittest.TestCase):
    def test_area_of_circle(self):
        self.assertAlmostEqual(area_of_circle(5), 78.54, places=2)

    def test_area_of_triangle(self):
        self.assertAlmostEqual(area_of_triangle(3, 4, 5), 6.0, places=2)

if __name__ == '__main__':
    unittest.main()