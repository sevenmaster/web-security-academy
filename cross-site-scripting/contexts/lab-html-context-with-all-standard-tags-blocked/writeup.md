The payload we are looking for is [this one](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet#onfocus).
I recently read online about custom tags with `onfocus` and where quite confident to solve this lab.
It took me some time to notice that the payload does not work in firefox, but still embedding it on the exploit server with `document.cookie` solves the lab.
