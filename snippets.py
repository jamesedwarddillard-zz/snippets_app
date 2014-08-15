"""
App for storing and retrieving snippets of text

-> need to add a get command
-> need to put in an error for snippets being called that haven't been created yet
-> need to make sure it works

"""

import logging
import csv
import argparse
import sys

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

def get(name, filename):
	"""Retrieving a snippet that has already been saved"""
	logging.info("Retrieving snippet called {}".format(name, filename))
	logging.debug("Opening file")
	with open(filename, "rb") as f:
		reader = csv.reader(f)
		logging.debug("Readng file for snippet".format(filename))
		data = {rows[1]:rows[0] for rows in reader}
		snippet = data[name]
	return name, snippet, filename


def make_parser():
	""" Construct the command line parser """
	logging.info("Constructing the parser")
	description = "Store and retrieve snippets of text"
	parser = argparse.ArgumentParser(description=description)

	subparser = parser.add_subparsers(help="Available commands")

	#Subparser for the put command
	logging.debug("Constructing put subparser")
	put_parser = subparser.add_parser("put", help="Store a snippet")
	put_parser.add_argument("name", help="The name of a snippet")
	put_parser.add_argument("snippet", help="The snippet of text to be stored")
	put_parser.add_argument("filename", default="snippets.csv", nargs ="?", help="The snippet filename")
	put_parser.set_defaults(command="put")

	#Subparser for the get command
	logging.debug("Constructing the get subparser")
	get_parser = subparser.add_parser("get", help="Retreive a snippet")
	get_parser.add_argument("name", help="The name of a snippet to be retreived")
	get_parser.add_argument("filename", default="snippets.csv", nargs="?", help="The snippet filename")
	get_parser.set_defaults(command="get")

	return parser

def main():
	""" Main function """
	logging.info("Starting snippets")
	parser = make_parser()
	arguments = parser.parse_args(sys.argv[1:])
	#Convert parsed arguments from Namespace to dictionary
	arguments = vars(arguments)
	command = arguments.pop("command")

	if command == "put":
		name, snippet = put(**arguments)
		print "Stored '{}' as '{}'".format(snippet, name)
	if command == "get":
		name, snippet, filename = get(**arguments)
		print "Retrieving '{}' from {}".format(name, filename)
		print "{}: {}".format(name, snippet)

if __name__ == '__main__':
	main()