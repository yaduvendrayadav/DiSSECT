import unittest
import ast
from dissect.traits.s07.s07 import s07_curve_function
from dissect.traits.example_curves import curve_names
results = {
    'secp112r2': {
        "{'weight': 1}": {
            'Arithmetic mean': 110.81298828125,
            'Geometric mean': 110.80341447843247,
            'Quadratic mean': 110.822411693636,
            'Harmonic mean': 110.79368643835123,
            'Variance': 3.3874580642803997,
            'Standard deviation': 0.5487515447890119}},
    'bn158': {
        "{'weight': 1}": {
            'Arithmetic mean': 156.25634765625,
            'Geometric mean': 156.2502599401067,
            'Quadratic mean': 156.26237607236507,
            'Harmonic mean': 156.2441119203337,
            'Variance': 2.640169461339223,
            'Standard deviation': 0.5270741095831041}},
    'brainpoolP160r1': {
        "{'weight': 1}": {
            'Arithmetic mean': 158.8701171875,
            'Geometric mean': 158.8635582172409,
            'Quadratic mean': 158.8766042896971,
            'Harmonic mean': 158.85692620411376,
            'Variance': 3.7373671343537413,
            'Standard deviation': 0.5954554294526033}}}


class TestS07(unittest.TestCase):

    def test_auto_generated_secp112r2(self):
        """This test has been auto-generated by gen_unittest"""
        params = ast.literal_eval(
            list(results["secp112r2"].keys())[0]).values()
        computed_result = s07_curve_function(curve_names["secp112r2"], *params)
        self.assertEqual(
            list(
                results["secp112r2"].values())[0],
            computed_result)

    def test_auto_generated_bn158(self):
        """This test has been auto-generated by gen_unittest"""
        params = ast.literal_eval(list(results["bn158"].keys())[0]).values()
        computed_result = s07_curve_function(curve_names["bn158"], *params)
        self.assertEqual(list(results["bn158"].values())[0], computed_result)

    def test_auto_generated_brainpoolP160r1(self):
        """This test has been auto-generated by gen_unittest"""
        params = ast.literal_eval(
            list(results["brainpoolP160r1"].keys())[0]).values()
        computed_result = s07_curve_function(
            curve_names["brainpoolP160r1"], *params)
        self.assertEqual(
            list(
                results["brainpoolP160r1"].values())[0],
            computed_result)


if __name__ == '__main__':
    unittest.main()
    print("Everything passed")
