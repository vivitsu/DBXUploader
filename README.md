Dropbox File Uploader
=====================

Upload a file to a Dropbox account from a URL.

Usage
-----

```shell
$ python3 main.py url
```
Dependencies
------------

The official Dropbox Python SDK, available [here](https://www.dropbox.com/developers/core/sdks/python). You can install
it system-wide, or setup a virtualenv and have it be local to the application directory.

Features
--------

* Will download file to the local machine, and then upload it to the linked Dropbox
* Uses OAuth2 authorization to link the application to the user's Dropbox, and for all requests made via the Dropbox API
* If application access has been revoked, it will retry after attempting to reauthorize the application

Caveats
-------

* In order to avoid exposing the `app_key` and `app_secret` provided by Dropbox, currently the program is setup to 
  read them from a separate config file. A sample config file is included with the source.
* Unfortunately, this means that if anyone wants to use this application, they
  will need their own `app_key` and `app_secret` in order to use this app. You can obtain them using the instructions
  found [here](https://www.dropbox.com/developers/support).
* Currently, the URL provided to the application is not parsed in a very sophisticated way, and can be further improved.
  See the source for URL formats which will work.
* If the file being uploaded already exists in the directory you are uploading to, a new copy will be created. A fix is
  in the works so that duplicates can be avoided.
  
Contributing
------------

Issue and PRs welcome.

License
-------

[Simplified BSD](http://opensource.org/licenses/BSD-2-Clause). See LICENSE file for more details.