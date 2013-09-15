# A [Flask](http://flask.pocoo.org) powered shadow hash generator using [Zurb Fundation](http://foundation.zurb.com) Bootstrap.

## Usage:
`$ python app.py`
Then visit `localhost:5000` in your browser.

A chicken or egg situation exists when creating user accounts on servers.
You can set their initial password for them, and force them to change it, or 
they can tell you what they want it to be and you can set it for them. Either
way, you are probably exchanging passwords.

Using shadow gen, you don't have to. The user simply enters their password, and then sends the generated salted hash to the person creating their server account. 

The has matches the pattern found in /etc/shadow. It currently supports md5 (those used on CentOS and RHEL).
