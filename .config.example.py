#!/usr/bin/env python
# NOTE: paths are relevant to the pb.py script

config = {
    "profile": {
        "username": "author",
        "homeland": "earth",
        "gender": "unspecified",
        "age": "33",
        "photo": "images/my-photo.png",
        "tagline": "I luv pepperonies, and cats and fluffy clouds",
        "bio": "I luv pepperoni so much that instead of walking around the block with a cigarette in my mouth I have a pepperoni, because I quite that awful habit :)  Did I mention I like cats?  Cats are cool!",
        "url": "https://the8woodcutter.sh"
    },
    "template_options": {
        "use_meta": True,
        "use_css": True,
        "use_extra_css": False,
        "use_js_head": False,
        "use_js_foot": False,
        "meta_location": "template/meta.html",
        "css_location": "template/blog.css",
        "css_extra_location": "template/extra.css",
        "js_head_location": "template/js_head.js",
        "js_foot_location": "template/js_foot.js"
    },
    "template_blocks": {
        "header_location": "template/header.html",
        "nav_location": "template/nav.html",
        "body_location": "template/body.html",
        "blogs_location": "template/blogs.html",
        "footer_location": "template/footer.html"
    },
    "blogs": {
        # Specify options for the blogs tuple
        "show_avatar": True,
        "show_flag": True
    }
}