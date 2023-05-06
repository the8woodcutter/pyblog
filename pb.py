#!/usr/bin/env python
import os
import re

class pb():

	global_config = ".config.py"
	global_config_default = {}

	def global_variables_check():
	# here we check if .config.py exists in root dir then fill in any required missing variables with defaults and set a dict() var of these variables
	# if file does not exist create the defaults
		# try open .config.py for reading and parse out it's syntax to dict()
		# except use dict(global_config_default)
		# return dict(global_variables)
		pass

# -------------------------------------------------------------------------
# HERE: future features:

	# def test_markdown():
	# # we are not necessarily going to use markdown, if we do we will remain pass and do later
	# 	pass

	# def markdown():
	# # remains a pass
	# 	pass

# -------------------------------------------------------------------------
# HERE: optional included html for parts of the html file generator functions:
# OPTIONAL!  

	# def google_analytics():
	# # optional includes
	# 	pass

	# def disqus_body():
	# # part of optional includes
	# 	pass

	# def disqus_footer():
	# # part of optional includes
	# 	pass

	# def twitter_card():
	# # part of optional includes
	# 	pass

	# def twitter():
	# # part of optional includes
	# 	pass

# -------------------------------------------------------------------------
# HERE: functions that generate html for included sections required in html rebuild functions below:
	# these return segments of html for other functions:

	def is_boilerplate_file():
		pass

	def tags_in_post():
	# an html included item
		pass

	def posts_with_tags():
	# an html included item
		pass

	def rebuild_tags():
		pass

	def get_post_title():
		pass

	def get_post_author():
		pass

	def list_tags():
		pass

	def list_posts():
		pass

	def get_html_file_content():
		pass

# -------------------------------------------------------------------------
# HERE: actual generation of html files:

	def make_rss():
		pass

	def rebuild_index():
	# rebuilds index
		pass

	def all_posts():
	# rebuilds posts index
		pass

	def all_tags():
	# rebuilds tags index
		pass

	def create_html_page():
		pass

	def create_includes():
		pass

	def delete_includes():
		pass

	def create_css():
		pass

	def date_version_detect():
		pass

	def rebuild_all_entries():
	# core function
		pass

	def parse_file():
	# does sanitization checks
		pass

# -------------------------------------------------------------------------
# HERE: the command line utility functions for this python script:

	def usage():
	# help info on command line or docstrings - include README in here
		pass

	def write_entry():
	# a function for opening a file or allowing on commandline writing of a post
		pass

	def edit():
	# same as write entry but only for commandline editing of post data as it is meant to be interpreted
		pass

	def reset():
	# core function
		pass

	def do_main():
	# executing this script as one function
		pass

# -------------------------------------------------------------------------
# HERE: run this script:
	# FIRE IN THE HOLE!
# if __name__ == __main__:
	# this jazz...