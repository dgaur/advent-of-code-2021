# Makefile for common AoC 2021 actions


# Run an individual AoC day.  Assumes each AoC day takes an external file of
# input
day%:
	@python3 $@.py < $@-data.txt


# Run all of the unittests
test:
	@python3 -m unittest *-test.py

