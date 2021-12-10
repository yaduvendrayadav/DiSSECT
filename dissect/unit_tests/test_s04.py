import unittest
import ast
from dissect.traits.s04.s04 import s04_curve_function
from dissect.traits.example_curves import curve_names
results = {
    'secp112r2': {
        "{'weight': 1}": {
            'Arithmetic mean': 110.863525390625,
            'Geometric mean': 110.84419046260417,
            'Quadratic mean': 110.89049785553512,
            'Harmonic mean': 110.82879326904343,
            'Variance': 1261.1726048541727,
            'Standard deviation': 1.8220765570357003}},
    'bn158': {
        "{'weight': 1}": {
            'Arithmetic mean': 156.30548095703125,
            'Geometric mean': 156.28619601690318,
            'Quadratic mean': 156.32974586085007,
            'Harmonic mean': 156.27031201144322,
            'Variance': 820.1035532159375,
            'Standard deviation': 2.0674474067506154}},
    'brainpoolP160r1': {
        "{'weight': 1}": {
            'Arithmetic mean': 158.946533203125,
            'Geometric mean': 158.9323510448994,
            'Quadratic mean': 158.9636906845544,
            'Harmonic mean': 158.92021846446352,
            'Variance': 495.3908499430973,
            'Standard deviation': 1.6565742610356027}}}


class TestS04(unittest.TestCase):

    def test_auto_generated_secp112r2(self):
        """This test has been auto-generated by gen_unittest"""
        params = ast.literal_eval(
            list(results["secp112r2"].keys())[0]).values()
        computed_result = s04_curve_function(curve_names["secp112r2"], *params)
        self.assertEqual(
            list(
                results["secp112r2"].values())[0],
            computed_result)

    def test_auto_generated_bn158(self):
        """This test has been auto-generated by gen_unittest"""
        params = ast.literal_eval(list(results["bn158"].keys())[0]).values()
        computed_result = s04_curve_function(curve_names["bn158"], *params)
        self.assertEqual(list(results["bn158"].values())[0], computed_result)

    def test_auto_generated_brainpoolP160r1(self):
        """This test has been auto-generated by gen_unittest"""
        params = ast.literal_eval(
            list(results["brainpoolP160r1"].keys())[0]).values()
        computed_result = s04_curve_function(
            curve_names["brainpoolP160r1"], *params)
        self.assertEqual(
            list(
                results["brainpoolP160r1"].values())[0],
            computed_result)


if __name__ == '__main__':
    unittest.main()
    print("Everything passed")
