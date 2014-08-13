"""
App for storing and retrieving snippets of text
"""

import logging
import csv
import argparse

#Set the log output file and the log level
logging.basicConfig(filename="output.log", level=logging.DEBUG)

def put(name,snippet,filename):
	"""Store a snippet with an associated name in the CSV file"""
	logging.info("Writing {}:{} to {}".format(name,snippet,filename))
	logging.debug("Opening file")
	with open(filename, "a") as f:
		writer = csv.writer(f)
		logging.debug("Writting snippet to file".format(name, snippet))
		writer.writerow([name, snippet])
	logging.debug("Write successful")
	return name, snippet

def make_parser():
	""" Construct the command line parser """
	logging.info("Constructing the parser")
	description = "Store and retrieve snippets of text"
	parser = argparse.ArgumentParser(description=description)

	return parser