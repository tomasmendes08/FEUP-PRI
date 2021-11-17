SHELL := bash

default: statistics

statistics: platforms
	python3 platforms.py

platforms: clean
	python3 statistics.py
	
clean: load
	python3 cleaning.py

load:
	python3 load_data.py
	