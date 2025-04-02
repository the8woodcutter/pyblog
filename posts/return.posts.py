#!/usr/bin/env python3
# This script is meant to return from a function a json formatted dictionary containing all of the posts as they are in `/pyblog_database`

import ../pb.py as pb
import ../database.py as run_db
import json
import os

class ReturnPosts():

	def __init__(self):
		
		blog_all = run_db.run()
		posts = [post for x in blog_all.get('posts')]
		json_posts = json.dumps(posts, indent=4)
		json_posts = str(json_posts)

		self.blog_all = blog_all
		self.posts = posts
		self.json_posts = json_posts

		# os.system(f"cat {json_posts} > ./posts.json")
		# os.system(f"cat {json_posts} > ./posts.json")
		# os.system(f"echo '{json_posts}' > ./posts.json")
		# os.system(f"echo '{json_posts}' > ./posts.json")
		os.system(f"echo {json_posts} > ./posts.json")
		os.system(f"echo {json_posts} > ./posts.json")

	def run(self):
		return self.json_posts
		# return str(self.json_posts)

	def run_all(self):
		self.blog_all = json.dumps(self.blog_all)
		return self.blog_all
		# return str(self.blog_all)