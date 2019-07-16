from unittest import TestCase
import unittest
from MaximumCombination import MaximumCombination


class test_MaximumCombination(TestCase):
    values = {
        "A": ["1", "2"],
        "B": ["X", "Y"],
        "C": ["Yes", "No"]
    }

    def test_ValuesExists(self):

        kys = [
            "A.C",
            "A.B",
        ]
        m = MaximumCombination(kys, self.values)
        js = m.getValueHash()
        self.assertEqual(js["total"], 0, "Failed")
        self.assertEqual(js["A"]["total"], 0, "Failed")
        self.assertEqual(js["A"]["1"]["C"]["total"], 0, "Failed")


if __name__ == "__main__":
    unittest.main()
