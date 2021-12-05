
# Run an individual AoC day
day%:
	python3 $@.py < $@-data.txt

# Run all of the unittests
test:
	python3 -m unittest *-test.py

