#!/usr/bin/env python
# THIS IS OLD NOW:

global_variables = {

    global_software_name:"BashBlog",
    global_software_version:"2.10",

    # Blog title
    global_title:"My fancy blog",
    # The typical subtitle for each blog
    global_description:"A blog about turtles and carrots",
    # The public base URL for this blog
    global_url:"http://example.com/blog",

    # Your name
    global_author:"John Smith",
    # You can use twitter or facebook or anything for global_author_url
    global_author_url:"http://twitter.com/example" ,
    # Your email
    global_email:"john@smith.com",

    # CC by-nc-nd is a good starting point, you can change this to "&copy;" for Copyright
    global_license:"CC by-nc-nd",

    # If you have a Google Analytics ID (UA-XXXXX) and wish to use the standard
    # embedding code, put it on global_analytics
    # If you have custom analytics code (i.e. non-google) or want to use the Universal
    # code, leave global_analytics empty and specify a global_analytics_file
    global_analytics:"",
    global_analytics_file:"",

    # Leave this empty (i.e. "") if you don't want to use feedburner, 
    # or change it to your own URL
    global_feedburner:"",

    # Change this to your username if you want to use twitter for comments
    global_twitter_username:"",
    # Default image for the Twitter cards. Use an absolute URL
    global_twitter_card_image:"",
    # Set this to false for a Twitter button with share count. The cookieless version
    # is just a link.
    global_twitter_cookieless:"true",
    # Default search page, where tweets more than a week old are hidden
    global_twitter_search:"twitter",

    # Change this to your disqus username to use disqus for comments
    global_disqus_username:"",


    # Blog generated files
    # index page of blog (it is usually good to use "index.html" here)
    index_file:"index.html",
    number_of_index_articles:"8",
    # global archive
    archive_index:"all_posts.html",
    tags_index:"all_tags.html",

    # Non blogpost files. Bashblog will ignore these. Useful for static pages and custom content
    # Add them as a bash array, e.g. non_blogpost_files:("news.html" "test.html")
    non_blogpost_files:(),

    # feed file (rss in this case)
    blog_feed:"feed.rss",
    number_of_feed_articles:"10",
    # "cut" blog entry when putting it to index page. Leave blank for full articles in front page
    # i.e. include only up to first '<hr>', or '----' in markdown
    cut_do:"cut",
    # When cutting, cut also tags? If "no", tags will appear in index page for cut articles
    cut_tags:"yes",
    # Regexp matching the HTML line where to do the cut
    # note that slash is regexp separator so you need to prepend it with backslash
    cut_line:'<hr ?\/?>',
    # save markdown file when posting with "bb post -m". Leave blank to discard it.
    save_markdown:"yes",
    # prefix for tags/categories files
    # please make sure that no other html file starts with this prefix
    prefix_tags:"tag_",
    # personalized header and footer (only if you know what you're doing)
    # DO NOT name them .header.html, .footer.html or they will be overwritten
    # leave blank to generate them, recommended
    header_file:"",
    footer_file:"",
    # extra content to add just after we open the <body> tag
    # and before the actual blog content
    body_begin_file:"",
    # extra content to add just before we close </body>
    body_end_file:"",
    # extra content to ONLY on the index page AFTER `body_begin_file` contents
    # and before the actual content
    body_begin_file_index:"",
    # CSS files to include on every page, f.ex. css_include:('main.css' 'blog.css')
    # leave empty to use generated
    css_include:(),
    # HTML files to exclude from index, f.ex. post_exclude:('imprint.html 'aboutme.html')
    html_exclude:(),

    # Localization and i18n
    # "Comments?" (used in twitter link after every post)
    template_comments:"Comments?",
    # "Read more..." (link under cut article on index page)
    template_read_more:"Read more...",
    # "View more posts" (used on bottom of index page as link to archive)
    template_archive:"View more posts",
    # "All posts" (title of archive page)
    template_archive_title:"All posts",
    # "All tags"
    template_tags_title:"All tags",
    # "posts" (on "All tags" page, text at the end of each tag line, like "2. Music - 15 posts")
    template_tags_posts:"posts",
    template_tags_posts_2_4:"posts",  # Some slavic languages use a different plural form for 2-4 items
    template_tags_posts_singular:"post",
    # "Posts tagged" (text on a title of a page with index of one tag, like "My Blog - Posts tagged "Music"")
    template_tag_title:"Posts tagged",
    # "Tags:" (beginning of line in HTML file with list of all tags for this article)
    template_tags_line_header:"Tags:",
    # "Back to the index page" (used on archive page, it is link to blog index)
    template_archive_index_page:"Back to the index page",
    # "Subscribe" (used on bottom of index page, it is link to RSS feed)
    template_subscribe:"Subscribe",
    # "Subscribe to this page..." (used as text for browser feed button that is embedded to html)
    template_subscribe_browser_button:"Subscribe to this page...",
    # "Tweet" (used as twitter text button for posting to twitter)
    template_twitter_button:"Tweet",
    template_twitter_comment:"&lt;Type your comment here but please leave the URL so that other people can follow the comments&gt;",
    
    # The locale to use for the dates displayed on screen
    date_format:"%B %d, %Y",
    date_locale:"C",
    date_inpost:"bashblog_timestamp",
    # Don't change these dates
    date_format_full:"%a, %d %b %Y %H:%M:%S %z",
    date_format_timestamp:"%Y%m%d%H%M.%S",
    date_allposts_header:"%B %Y",

    # Perform the post title -> filename conversion
    # Experts only. You may need to tune the locales too
    # Leave empty for no conversion, which is not recommended
    # This default filter respects backwards compatibility
    convert_filename:"iconv -f utf-8 -t ascii//translit | sed 's/^-*//' | tr [:upper:] [:lower:] | tr ' ' '-' | tr -dc '[:alnum:]-'",

    # URL where you can view the post while it's being edited
    # same as global_url by default
    # You can change it to path on your computer, if you write posts locally
    # before copying them to the server
    preview_url:"",

    # Markdown location. Trying to autodetect by default.
    # The invocation must support the signature 'markdown_bin in.md > out.html'
    # [[ -f Markdown.pl ]] && markdown_bin:./Markdown.pl || markdown_bin:$(which Markdown.pl 2>/dev/null || which markdown 2>/dev/null)
}