#!/usr/bin/env python3
# This script is meant to return from a function a json formatted dictionary containing all of the posts as they are in `/pyblog_database`

import pb.py

class ReturnPosts():

	def __init__(self):
		
		blog_all = run_db.run() # wtf does this?
		
		posts = [post for x in blog_all.get('posts')]
		json_posts = pb.json.dumps(posts, indent=4)
		json_posts = str(json_posts)

		self.blog_all = blog_all
		self.posts = posts
		self.json_posts = json_posts

		# later we need this in a dictionary:
		os.system(f"echo {json_posts} > ./posts.json")

	def run(self):
		# can try to take ./posts.json and parse it into dict():
		return self.json_posts
\
	def run_all(self):
		new_blog_all = json.dumps(self.blog_all)
		return new_blog_all