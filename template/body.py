<!-- This is the HTML markup for a post -->
import os

def post(title,author,badges,post_date,body,rating):
	os.system(f"touch ../posts/{title}.html")
	post = open('../posts/{title}.html', 'w')
	"<big><a href='{title}'><big>" :: <small>{author}</small> <sup>{for b in badges:  print("<img src='{b}'\>")</sup>" + f"<br/><i>{post_date}</i>)----------------------------") + f"<br/><p>    {body}</p>"