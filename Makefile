SHELL := bash

default: statistics

statistics: clean
	python3 src/statistics.py
	
clean: load
	python3 src/cleaning.py

load:
	python3 src/load_data.py
	
clean:
	rm -rf dev/*