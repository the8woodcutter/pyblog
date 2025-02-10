#!/usr/bin/env python3
# NOTE: paths are relevant to the pb.py script

config = {
    "software": "PyBlog",
    "software_version": "v0.1",
    "author": "the8woodcutter",
    "global_title": "My Python Blog",
    "global_description": "A blog about astronauts eating pepperoni!",
    "global_url": "http://astronuts.sh/blog",
    "global_licence": "TBD",

# FEATURES' VARS:
    "twtxt": {
    # NOTE: this info was derived from yarn.social style twtxt.txt files!
        "nick": "author",
        "url": "http://astronuts.sh/twtxt.txt",
        "prev": "at this moment i don't know what this is/does",
        "avatar": "http://astronuts.sh/images/avatar.png",
        "following": 3781,
        # "links": ["https://yahoo.ca","https://the8woodcutter.sh","https://xe.com"],
        # "follows": ["akoizumi https://social.chaotic.ninja/user/akoizumi/twtxt.txt","chunkimo https://twtxt.net/user/chunkimo/twtxt.txt"],
        # "posts": ["2023-04-21T00:00:00Z\tMy post!  I says!"]
    },
    "google_analytics": {
        # Optional
    },
    "fediverse": {
        # Optional
        "webfinger": "@chunk@mstdn.social"
    }
    "twitter": {
        # Optional
    },
    "feedburner": {
        # Optional
    },
    "disqus": {
        # Optional
    },
    "gravatar": {
        # Optional
        "email": "", # "author@gravatar.place"
    },
    "avatarimg": {
        "url": "", # "https://the8woodcutter.sh/img/pyblog/chunk/profile/my_avatar.png",
    },


# PAGE ELEMENTS:
    "profile": {
        "username": "", # "root",
        "photo": "", # "images/my-photo.png",
        "tagline": "", # "I luv pepperonies, and cats and fluffy clouds",
        "homeland": "", # "earth",
        "age": "", # "33",
        "gender": "", # "unspecified",
        "bio": "", # "I luv pepperoni so much that instead of walking around the block with a cigarette in my mouth I have a pepperoni, because I quite that awful habit :)  Did I mention I like cats?  Cats are cool!",
        "url": "", # "https://the8woodcutter.sh",
        "email": "", # "mailto:author@astronuts.sh",
        "xmpp": "", # "xmpp:stackvice@packets.cc",
        "tags": [], # ["xmpp","hardrave","computing","linux","networking","car audio","progress","pyblog","cybersecurity"],
    },
    "template_options": {
        "use_meta": True,
        "use_css": True,
        "use_header": True,
        "use_nav": True,
        "use_footer": True,
        "use_js_head": False,
        "use_js_foot": False,
        "use_profile_page": False,
    },
    # all of the other html files go into body.html
    "pages": {
        "blogs_location": "template/root/",
        "profile_location": "template/profile/",
    }
}