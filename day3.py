# AoC 2021, day 3
# https://adventofcode.com/2021/day/3

import sys

class Diagnostic(object):
    def __init__(self, reports):
        (self.gamma, self.epsilon) = self.parse_reports(reports)
        return

    def parse_reports(self, reports):
        gamma = 0
        epsilon = 0

        # Halfway threshold for computing "most common bit" for gamma
        half = len(reports)/2

        # Compute each bit of the gamma value, one at a time
        for shift in range(5):  # Assume 5-bit fields, from AoC example
            mask = (0x1 << shift)

            # Which reports have this bit set?
            asserted_reports = [ r for r in reports if (r & mask == mask) ]
            #print(mask, len(asserted_reports))

            # Infer the next bits of gamma
            if (len(asserted_reports) >= half):
                gamma |= mask
            else:
                epsilon |= mask     # Invert gamma, but only 5-bit field

        return (gamma, epsilon)


    def read_power_consumption(self):
        return self.gamma * self.epsilon



if __name__ == "__main__":
    # Convert text input to numeric equivalent
    parsed_reports = [ int(r, base=2) for r in sys.stdin ]

    diag = Diagnostic(parsed_reports)
    print(diag.read_power_consumption())


