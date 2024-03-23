import unittest
from task_2.geom_calc import Circle, Triangle

class TestGeometryCalculations(unittest.TestCase):
    def test_area_of_circle(self):
        self.assertAlmostEqual(Circle(5).area(), 78.54, places=2)

    def test_area_of_triangle(self):
        self.assertAlmostEqual(Triangle(3, 4, 5).area(), 6.0, places=2)

if __name__ == '__main__':
    unittest.main()