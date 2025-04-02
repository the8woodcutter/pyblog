## `PyBlog v0.1`

### Python3 weblog site generator script -- Single script to create and manage a blog using only python and text files
#### I intend to redo bashblog ([github.com/the8woodcutter/bashblog](https://github.com/the8woodcutter/bashblog)) in python to do essentially the same thing
* Author: the8woodcutter || [my XMPP](xmpp:chunk@toofast.vip) || [XMPP room](xmpp:the-subnet@chat.toofast.vip?join)
* Licence: DO NOT COPY (_until licence decided_)

---

### `Ideas`
* I've decided to make a **REDO** not a **REWRITE** as if rewriting is more like copying bashblog code methods (1 for 1 even?), and redoing is copying end result
* Additional feature ideas include a profile self object with variables and avatar (optionally gravatar is an option) for personification,
	* Editable CSS blocks for seperation of spacing, colors, text, block objects, etc **OPTIONAL**
	* Templates segmented more, include javascript, metadata, css, header, nav, body, footer, javascript_head and javascript_footer blocks **OPTIONAL**
	* An attempt of simple to read script and simple function structure
	* Simple seperation from default (easy/simpler) stuff and more involved stuff; perhaps a first run function?  _!Python not to install packages!_
	* RSS automagic using lists that reuses data for twtxt.txt, twtxt.txt we want to maybe use yarn.social extensions?  Webhooks!  APIs!  LoL :D
	* Use of python for ANYTHING functional but when used as a script
* More to come

## `TODO:`
* There needs to be a planned database structure (using the python shelve / pickle scheme, no sql or external db needed)
	* How to represent this even as a code comment block???
* the REAL next thing we do is...  decide what page types, ie: main index, tags, categories, profile, post index, rss index, etc
	* make drawing of the blog intended structure 0-100% (_filling things in as we go_)
* conjuring of the profile functions and file structure, as well as which ephemeral files/dirs are needed for what (tinker it up foo)
	* if it's a page, distinct outside of blog page, it can be unified itself, and borrow CSS from `templates/default/*/*` as defaults.

---

### `Need help or have a comment then feel free to submit an issue.`

---

## Instructions:
do:
	- ~python3 python config.py
	- fill out the config.py with your data, at least read it
	- [optional]: cp any `/templates/default/*/*.html` to `/templates/custom/*/` for overiding HTML and CSS things
	- make a post using `python3 pb.py post`
	- Highly recommended to change some of the HTML / CSS from default (which you can see all in `/templates/default/*/*`)
		- cp to `/templates/custom/*/*` then change in `/*/custom/*/*`
nginx/apache2/httpd:
	- all pages by the scheme have index.html files that will make the URL `/vlogs/index.html` as `/vlogs/`
	- howevwer for SEO sake `/posts/i-am-a-post-page.html` is how posts will be represented
	- tags should use `index.html` but tag name should be at `/tags/{tag_name}/index.html` while presenting as `'/tags/{tag_name}/`
		- how do we do this??? *scratching head*

---
