# A [Flask](http://flask.pocoo.org) powered shadow hash generator using [Zurb Fundation](http://foundation.zurb.com) Bootstrap.

## Usage:
`$ python app.py`
Then visit `localhost:5000` in your browser.

A chicken or egg situation exists when creating user accounts on servers.
You can set their initial password for them, and force them to change it, or 
they can tell you what they want it to be and you can set it for them. Either
way, you are probably exchanging passwords.

Using shadow gen, you don't have to. The user simply enters their password, and then sends the generated salted hash to the person creating their server account. 

The hash matches the pattern found in /etc/shadow. It currently supports md5 (those used on CentOS and RHEL).

If you combine this with only allowing public key authentication, you can set user's passwords without actually
needing to know their passowrds.

It is essentially `$ python -c "import crypt; print crypt.crypt('mypasswordhere', '\$1\$SALTsalt')"` but in an easy to
use webapp for users.

The output from the above command would look like this:

`$1$SALTsalt$z6ZRnfeJvg.EiK/Enyl.k0`

It doesn't store any passwords or keys and each time it is used, a random salt is generated to create the hash.

The `/etc/shadow` file looks like this:

    daemon:*:15513:0:99999:7:::
    adm:*:15513:0:99999:7:::
    lp:*:15513:0:99999:7:::
    sync:*:15513:0:99999:7:::
    shutdown:*:15513:0:99999:7:::
    halt:*:15513:0:99999:7:::
    mail:*:15513:0:99999:7:::
    uucp:*:15513:0:99999:7:::
    operator:*:15513:0:99999:7:::
    games:*:15513:0:99999:7:::
    gopher:*:15513:0:99999:7:::
    ftp:*:15513:0:99999:7:::
    nobody:*:15513:0:99999:7:::
    mike:$1$SALTsalt$z6ZRnfeJvg.EiK/Enyl.k0:15961:0:99999:7:::
    
Using the hash, you can set the user "mike's" password: `mike:$1$SALTsalt$z6ZRnfeJvg.EiK/Enyl.k0:15961:0:99999:7:::`

You can try it out at [shadow.heyhomeslice.com(http://shadow.heyhomeslice.com)

*NOTE:* To generate proper shadow hashes, this app should be run on a linux machine. OS X doesn't handle the hasing
properyly. You can still run the app on OS X, just don't expect your passwords to actually work when you put them in
your `/etc/shadow` file.

