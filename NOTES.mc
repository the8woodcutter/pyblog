***

## NOTES:
## MODE OF OPERATION:: KEEP SIMPLE, GET DONE, EXPAND LATER!

### OMIT JAVASCRIPT NOW
	* We are not dealing with JS at this time

#### Program Flow:
	* User has no blog posts, starts a post
		* new_post()
	* User wants to edit post
		* edit_post()
	* User wants to reset blog to default
		* Needs DEFAULT_CORE_FILES
		* reset()
	* User changes some .css and some .js files, doesn't know if it'll work then starts a post
		* new_post() // this will add the post as a file
		* rebuild() // this will add all of the CONFIGURED? .css, .html, .tag, .comment files in CHRONOLOGICAL ORDER EACH into 			their respective index.html files

#### .tag, .comment FILES:
	* .tag files will be micro db's that will be appended to the paths of any posts (of future other) using this existing .tag
		* tag exists based on .tag file being TAG_NAME.tag simply
	* .comment files will be also micro db's where at first is the post pathname then an index in comment list then anonymous 				user (later on we will use XMPP users with HTTP API) then datetime then comment then stars count

#### Functions we require and in what order:
	* new_post()
	* edit_post()
	* reset()
	* rebuild()
// REALISTICALLY THIS IS ALL THAT BB.SH DOES

***