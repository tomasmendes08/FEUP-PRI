SHELL := bash

default: statistics

statistics: clean
	python3 statistics.py
	
clean: load
	python3 cleaning.py

load:
	python3 load_data.py
	