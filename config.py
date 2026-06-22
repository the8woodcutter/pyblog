#!/usr/bin/env python3
# NOTE: a relative path will be for example: `posts/` and an absolute path would be `/templates/default/css`
# ..  to reference the same `/templates/default/css` but relatively from in any file in 
# ..  the WEBROOT (webserver configured root directory) `/` the relative
# ..  path is `../template/defaults/css` and from in a file in the project directory it's just `templates/default/css`
###
# NOTE: the webroot is expected to be `/public/` and the project root (root of this file here) is `/` in relation to
# ..  this project and the directories named throughout it.  One is not supposed to publicly have pb.py in their WEBROOT
# ..  the8woodcutter thinks this would be good practice

config = {
    "software": "PyBlog",
    "software_version": "v0.1",
    "author": "Bloggist Machine of Bloggery",
    "global_title": "My Python Blog",
    "global_description": "A blog about astronauts eating pepperoni!",
    "global_url": "http://astronuts.sh/blog",
    "global_licence": "GPL",

# FEATURES' VARS:
    "twtxt": {
        # Optional
        # "url": "http://domain.tld/twtxt.txt",
    },
    "google_analytics": {
        # Optional
        # !! Requires a something, I can't recall what
    },
    "fediverse": {
        # Optional
        # "webfinger": "@username@mstdn.xxx"
    }
    "libravatar": {
        # Optional
        # "email": "author@email.addr"
    }
    "gravatar": {
        # Optional
        # "email": "", # "author@email.addr"
    },
    "avatarimg": {
        # Optional
        ## Prefer PNG **ONLY** for sake of, best format ever and XMPP compliance woes
        # "url": "https://domain.tld/avatar.png"
    },


# PAGE ELEMENTS:
    # "profile" Optional, this will be enabled if at bottom "profile_location" is not empty

    # "profile": {
    # All of these are optional
        # "username": "", # "root",
        # "photo": "", # "images/my-photo.png",
        # "tagline": "", # "I luv pepperonies, and cats and fluffy clouds",
        # "homeland": "", # "earth",
        # "age": "", # "33",
        # "gender": "", # "unspecified",
        # "bio": "", # "I luv pepperoni so much that instead of walking around the block with a cigarette in my mouth I have a pepperoni, because I quite that awful habit :)  Did I mention I like cats?  Cats are cool!",
        # "url": "", # "https://the8woodcutter.sh",
        # "email": "", # "mailto:author@astronuts.sh",
        # "xmpp": "", # "xmpp:e@packets.cc",
        # "tags": [] # ["xmpp","hardrave","computing","linux","networking","car audio","progress","pyblog","cybersecurity"],
    # },

    
    "template_options": {
        # These are defaults, no changes are necessary but optional
        ## !!! THESE OPTIONS MATCH THE DIRECTORIES IN /templates SO USE ACCORDINGLY !!!
        "use_meta": True,
        "use_css": True,
        "use_header": True,
        "use_nav": True,
        "use_footer": True,
        "use_js_head": False,
        "use_js_foot": False,
        "use_profile_page": False, # We will not construct this schematic early on
        "use_twtxt_page": False, # To be implemented later on as deafault twtxt front end
        "use_fediverse_page": False # I consider making this just an iframe to their own page
        ## IDEA: perhaps adding in this area, from other files/dirs where CSS and precise widget HTML formatting is also configured, some ...
        ## ... profile widgets but for various any other place.  Discord, Instagram, Youtube, all those and many more, if they don't anymore, ...
        ## ... they certainly likely used to give you a HTML embed of some of your profile info.
        ## IMPORTANT THINGS: we DO wish to keep internet COOL by PROPER use of personification, of one's place on the web!!
        ### ^ truly magical, we will work with this in our time and make fortified acceptance with no boundaries creatively, with pyblog.
        #### HUMONGOUS SPOILER: this I write for a particular person, in the event they actually read this: the XMPP simple IM chat web widget.
    },
    "pages": {
        "blogs_location": "posts/", 
        "profile_location": "profile/",
        "twtxt_location": "twtxt/"
        ""
    }
}