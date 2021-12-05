
import unittest
from day3 import Diagnostic


class TestDiagnostic(unittest.TestCase):
    def test_empty_reports(self):
        """Base case of zero reports"""
        d = Diagnostic([])
        assert(d.read_power_consumption() == 0)
        return

    def test_sample_reports(self):
        """Base case of zero reports.  Verbatim from the AoC example"""
        d = Diagnostic([
            0b00100,
            0b11110,
            0b10110,
            0b10111,
            0b10101,
            0b01111,
            0b00111,
            0b11100,
            0b10000,
            0b11001,
            0b00010,
            0b01010,
        ])
        assert(d.gamma == 22)
        assert(d.epsilon == 9)
        assert(d.read_power_consumption() == 198)

        return

if __name__ == "__main__":
    unittest.main()
