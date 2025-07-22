# tests/test_analyzer.py
import unittest
from analyzer import evaluate_password

class TestPasswordAnalyzer(unittest.TestCase):
    def test_strong_password(self):
        result = evaluate_password("Str0ng!Passw0rd")
        self.assertGreaterEqual(result["score"], 60)

    def test_weak_password(self):
        result = evaluate_password("password")
        self.assertLess(result["score"], 40)

    def test_entropy(self):
        result = evaluate_password("Aa1!Aa1!Aa1!")
        self.assertTrue("entropy" in result)

if __name__ == '__main__':
    unittest.main()