from typing import List
from dissect.traits import Trait


TRAIT_TIMEOUT = 30

def near_order_factorizations(n, sign="+", k=10, t=10):
    """Computer factorization of k*n+1 (k*n-1) if 'sign' is "+" ("-") in time 't' """
    from dissect.utils.utils import Factorization

    assert sign in ["+", "-"]

    if sign == "+":
        m = k * n + 1
    else:
        m = k * n - 1
    return Factorization(m, timeout_duration=t).factorization()


def largest_factor_bitlen(factorization):
    """Computes bit length of largest factor(last item of list) of 'factorization' """
    if isinstance(factorization, str):
        return factorization
    else:
        return factorization[-1].nbits()


class KNFactorizationTrait(Trait):
    NAME = "kn_factorization"
    DESCRIPTION = "Factorization of $kn \\pm 1$ where $n$ is the cardinality of the curve."
    INPUT = {
        "k": (int, "Integer")
    }
    OUTPUT = {
        "(+)factorization": (List[int], "Factorization of $kn + 1$"),
        "(+)largest_factor_bitlen": (int, "Largest factor of $kn + 1$"),
        "(-)factorization": (List[int], "Factorization of $kn - 1$"),
        "(-)largest_factor_bitlen": (int, "Largest factor of $kn - 1$")
    }
    DEFAULT_PARAMS = {
        "k": [1, 2, 3, 4, 5, 6, 7, 8]
    }

    def compute(curve, params):
        """
        Computes factorization of ord*k+1 and ord*k-1 and bit lengths of their largest factors
        Returns a dictionary
        """

        card = curve.cardinality()
        t = TRAIT_TIMEOUT
        curve_results = {"(+)factorization": near_order_factorizations(card, "+", params["k"], t)}
        curve_results["(+)largest_factor_bitlen"] = largest_factor_bitlen(
            curve_results["(+)factorization"]
        )
        curve_results["(-)factorization"] = near_order_factorizations(card, "-", params["k"], t)
        curve_results["(-)largest_factor_bitlen"] = largest_factor_bitlen(
            curve_results["(-)factorization"]
        )
        return curve_results


def test_kn_factorization():
    assert True
