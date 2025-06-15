#!/usr/bin/env python3
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

class pb():

	import os
	import re
	import random
	import json
	import datetime
	import database.py as run_db


## The segments of functions, meaning groups of functions:
### Configuration options!!!!, Post Actions (post, edit, delete), blog actions (reset, rebuild), guide actions (initial tutorial/help text), features actions (selecting features function, core features implementation functions)
#
## Core features are going to be:
### NOTHING!  At first anyhow
### 	* Google Analytics,
###		* Visitor Counter,
###		* Clock,
###		* likes counter (ajax),
###		* webring,
###		* blog owner profiles,
#
##	Afterwards Modules that can be Added:
###		* web interface to create / edit / delete posts
###		* twtxt microblogging page / implementation
###			* XMPP PubSub and/or MQTT (PubSub) binding to twtxt entries
###			* every which direction has the same capabilities, to publish and to subscribe
###			* however as far as administering and deleting posts, not sure yet...
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# NOTES:
# * run_db.run()
# 	* will run ./database.py and return pyblog_database.get('blog_all') as it is a dict()

	def __init__(self, args):
	# The variables we should declare here are from the config yes?
		self.args = args
		self.todaysday = datetime.date.today()
		self.timestamp = datetime.today.strftime("%B %d, %Y")
		# we want as variables in dictionary 'blog_all' from database
		blog_all = run_db.run()
		self.blog_all = blog_all

# ---------------------------------------------------------------------------------------------------

	# def read_file():
	# # this simple reads the segment/file
	# # is part of preparing for an edit post.
	# 	pass

	# def build_file():
	# # building a file, or do we build all the files?
	# # This is for building an HTML file from the segments
	# 	pass

	# def check_file():
	# # How to check an HTML/CSS files for syntax?
	# # Do we run a test of some kind?
	# 	pass

# ---------------------------------------------------------------------------------------------------

	# def mod_title():

	# def mod_tags():
	# 	tags = []		

	# def mod_author():
	# 	author = input("Who is the author?  Or 'skip' for default")
	# 	return author

# ---------------------------------------------------------------------------------------------------

	# ### THIS SECTION IS FOR POST MANIPULATION!!!!

	def query_post_it(self, post_content):
	# Function to ask after post made what to do with post:
		sel = input("Choose whether you want to save as draft or post or edit again: (d, p, e ) pls choose a letter only..")
		if sel == "d":
			os.system(f"cat {post_content} > ./drafts/")

	def edit_post(self, filename):
	# using exact .html filename in full will allow you to modify the portion of the body of the post and the title
		postnames = os.listdir('./posts/')
		if filename in postnames:
			os.system(f"cp ./posts/{filename} ./drafts/")
			os.system(f"$EDITOR ./drafts/{filename}")
		pass
	def create_post(post_content)
		with shelve.open('pyblog_database') as db:
			blog_all = db.get('blog_all')
			posts = db.get('blog_all').get('posts')
			posts_tags = db.get('blog_all').get('posts').get('tags')
			posts_media = db.get('blog_all').get('posts').get('media')
			tags = db.get('blog_all').get('tags')

		db.close()
	def new_post():
	# This will open up an editor (ie: nano) for creation of post xtitle, post author, post, then tags
		# What to ask or tell the client before opening their $EDITOR
		def publish_post():
			post_content = os.open('./drafts/new_post.html','r')
			post_content = post_content.read()
			post_content.close()
			sel = input("Post this post to the blog?  y/n")
			if sel == "y" or sel == "Y":
				create_post(post_content)
		prompt = "Create a post using HTML?  y/n"
		sel = input(prompt)
		if sel == "y" or sel == "Y":
			cmd = "$EDITOR ./drafts/new_post.html"
			os.system(cmd)
		elif sel == "n" or sel == "N":
			print("No post?  No more options, exiting...")
			pause(2)
			exit()
		else:
			print("What?  Y (the letter, meaning yes) or N (also a single alpha meaning no)")
			prompt = "Create a post using HTML?  y/n"
			sel = input(prompt)
			if sel == "y" or sel == "Y":
				cmd = "$EDITOR ./drafts/new_post.html"
				os.system(cmd)
			elif sel == "n" or sel == "N":
				print("No post?  No more options, exiting...")
				pause(2)
				exit()
			else:
				print("Function does not exist.  Exiting...")
				pause(2)
				exit()


	def rebuild():
	# here we will rebuild all the blog posts,
	# tag, posts, about, etc pages using the already generated timestamps and relevancies (tags, categories)
		pass

	def reset_all():
		# Resets to original theme template, AND, erases all tags, dates, posts and profile data, in fact when ever anything at all
		# ... that adds to this need to be reset is added to this program it needs to be deleted from using trhis function
			# One must not delete images or audio or video files or any files not textual files related to posts.
		pass

	def reset_template():
	# we will just load the default CSS in place of the custom CSS and zip the old CSS for user sake
	# This does NOT delete personalized data
		# SHOULD DO A A DIFF ON OLD <head>content</head> (and etc) vs new content and if newer than old content to then mkdir for
		# a template backup snippets and cop all the text differeing from stock theme html
		pass

	def help():
	# Here we will just go through the README in depth and explain wtf to do here :)
	# This is likely going to be a lengthy bunch of text that has to take user input.
	# It should be fulfilled over the course of building this app
		pass

#	def edit_profile():
#	# PROFILES ARE YET TO BE DECIDED!
#		pass

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