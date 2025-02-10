---

# NOTICE:
## Are you doomed?  Read this:
## WHATEVER YOU PUT IN THESE FILES IS RENDERED ON **YOUR** SITE, IT'S YOUR PROBLEM IF YOU WRITE BAD AND DON'T FOLLOW THE SCHEME OR SCREW UP MODIFYING THE SCHEME
### Options for support in the unfortunate chance that you've mutilated this script beyond all repair are:
	* to run `/pb.py reset-template` to use default html stuff
	* to run `/pb.py reset` to destroy all your posts, tags, profile, and every last thing that pyblog did not give you for xmas when you opened it
	* to batphone bill gates and get his rich ass to send you an apache helicoptor at once with 5 soydevs that don't know shit to spend 6 hours adding javascript to your easy as f to use pyblog
	* go back to school and learn to read
	* use stack overflow
	* try wordpress and end up calling a tech for that too
	* use codeacademy and learn how to read english if you already have a hard time reading the verbose documenting in pyblog
	* move to india and learn front end web development and become soyest of the soydevs
		* while simultaneously destroying mainstream internet with javascript web apps that I cannot load whatosever on my phone using VPN
	* delete pyblog and get a godaddy website
	* if you have a feature request, a pull request (are welcome to consideration) or an idea, please do get an XMPP client to jump on XMPP network and add <a href="xmpp:chunk@toofast.vip">chunk@toofast.vip</a> as contact then probe me at will, make it sexxy but don't overdo it, for sexxy talk females only, furries considered based on character

# Notice:
## Do you need motivation?  Read this:
#### PYTHON IS GREAT, SO ARE WEB LANGUAGES, LEARN THEM AND YOU CAN UNDERSTAND THEN BECOME YODA, THERE IS NO TRY, THERE IS ONLY DO **AMAZE**
#### You are amaze yes?  That's the spirit and the stuff of magnificient people, one should aspire to be **amaze** and learn the web languages and the pythons, yes

---

### HAVING FUN?
#### IF MY BLOG IS UP CHECK IT OUT: __<a href="https://the8woodcutter.sh/blog" target="_blank">the8woodcutter.sh</a>__

***

#### __this is the file structure and base apparatus for the `/pb.py rebuild` and `/pb.py reset` and `/pb.py reset-template`__
#### -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### _WHERE `{pageurl}/` EXISTS IS IN THIS DIRECTORIES ROOT ARE DIRECTORIES NAMED REPRESENTING THE PAGE IN THE PYBLOG_
#### _IF YOU WANT TO ADD A PAGE, YOU MUST COPY ALL OF THE SAME DIRECTORIES AND THEIR INCLUDED FILES FROM WHERE APPROPRIATE EITHER `../custom/` or `.#default/`_
### _YOU CANNOT ADD WILLY NILLY WHAT YOU WANT AS NEW FILES OR DIRECTORIES, ONLY EDIT THE FILES `{pageurl}/head/meta.html` AS ONLY `<meta>` TAGS!!!_
### _`{pageurl}/head/` THIS MEANS `<head>` AND `{pageurl}/head/*.html` THE `*` IS THE TAG YOU CAN MODIFY!!!_
#### _NEED I REMIND YOU THAT YOU CANNOT ADD OTHER TAGS, UNLESS YOU ADD THEM TO THE CONSTRUCTOR FUNCTION THAT REBUILDS/RESETS THE PYBLOG_
### _SO `{pageurl}/head/meta.html` YOU MODIFY ONLY `<meta>` TAGS INSIDE OF `<head>` TAGS LIKE THIS: `<head><meta>` AND IT WILL BE AT URL `{pagurl}/<HTML TAGS FOR THIS INDEX FOR THIS PAGE URL>`_
### _AND `{pageurl}/` CAN ONLY EXIST AT `/` OR ROOT OF WEBROOT.  IN ORDER TO MODIFY THIS **CHECKED FOR** SCHEME YOU MUST MODIFY THE CHECK FUNCTION AND WHERE'S WALDO?_
### _IMPORTANT: YOU MUST WRITE THE ENTIRE `*` TAG YOU'RE ADDING ONE EACH PER LINE PER TAG ITEM WITH OPENING AND CLOSING TAGS INCLUDING THE REQUIRE AND ALSO IF NEEDED SUPPORTED ATTRIBUTES_
### _HOWEVER FOR MULTIPLE TAGS THE PUTTING THEM EACH ON NEWLINES ONLY MAKES YOUR CODE MORE READABLE, LINE SEPERATION IS IGNORED WHEN BUILDING_

#### I wonder what html tastes like, sounds crunchy ...  maybe salty, or spicy, I just can't guess ...

## ALL NEW DIRECTORIES OR FILES AND MISUSE OF THIS SCHEME WITHOUT PROPER APPLICATION CHANGES CONSIDERED FOR THE SCHEME ARE IGNORED AND THE USER WILL BE DOOMED TO THE BEGINNING OF THIS README

***
