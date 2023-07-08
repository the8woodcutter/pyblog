#!/usr/bin/env python
# Author: chunk@toofast.vip -- The 8 Woodcutter -- github.com/the8woodcutter/pyblog -----------------
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

	# NEW GAMEPLAN!
	# We want logic of what the program acheives, not logic of how the program achieves achievement.
	# A redo not a rewrite of bashblog.
		# Templates include metadata, javascript, css, header, nav, footer
		# CSS templates break up for: TBD
		# Features include: disqus, google analytics, rss, twtxt, avatar, profile/about page ...
		# ... editable nav links

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

import os
import re
from random import randint

class pb():
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

	def __init__():
	# The variables we should declare here are from the config yes?
		pass

# ---------------------------------------------------------------------------------------------------

	def read_file():
	# this simple reads the segment/file
	# is part of preparing for an edit post.
		pass

	def build_file():
	# building a file, or do we build all the files?
	# This is for building an HTML file from the segments
		pass

	def check_file():
	# How to check an HTML/CSS files for syntax?
	# Do we run a test of some kind?
		pass

# ---------------------------------------------------------------------------------------------------

	def mod_title():
		

	def mod_tags():
		tags = []		

	def mod_author():
		author = input("Who is the author?  Or 'skip' for default")
		return author

# ---------------------------------------------------------------------------------------------------

	def edit_post():
	# using exact .html filename in full will allow you to modify the portion of the body of the post and the title
		pass

	def edit_profile():
	# PROFILES ARE YET TO BE DECIDED!
		pass

	def new_post():
	# This will open up an editor (ie: nano) for creation of post title, post author, post, then tags


	def new_post_file():
	# This will ask for an .html file in a directory under the webroot/drafts and then ask for tags to add
		pass

	def rebuild():
	# here we will rebuild all the blog posts,
	# tag, posts, about, etc pages using the already generated timestamps and relevancies (tags, categories)
		pass

	def reset():
	# We will use a default 1 post
	# ...default CSS file
	# ...default profile
	# ...not use any commenting or otherwise
	# ...we will rewrite the namesake vars and other vars with defaults
	# This will all be unloaded from a default.zip
		pass

	def reset_template():
	# we will just load the default CSS in place of the custom CSS and zip the old CSS for user sake
		pass

	def help():
	# Here we will just go through the README in depth and explain wtf to do here :)
		pass

# ---------------------------------------------------------------------------------------------------

if __name__ == '__main__':
	print("Which option would you like?")
	greetings = [
		"SELECT ONLY ONE:",
		"1-> To create an HTML post",
		"2-> To user an already HTML post file (full path)",
		"3-> To edit an HTML file",
		"4-> To edit your profile details",
		"5-> To rebuild your code base and all your pages (useful for testing styles and such)",
		"6-> To RESET to DEFAULT your entire website",
		"7-> To RESET all the CSS/Styles",
		"8-> HELP ME!!!"
		]

	for x in greetings:
		print(x)
	option = input("Your Choice?")

	try:
		if len(option) == 1 and is_int(option) and option < 8 and option > 0:
			if option == 1:
				new_post()
			if option == 2:
				new_post_file()
			if option == 3:
				edit_post()
			if option == 4:
				edit_profile()
			if option == 5:
				rebuild()
			if option == 6:
				reset()
			if option == 7:
				reset_template()
			if option == 8:
				help()
	except:
		print('Incorrect Input aborting!')
		exit()