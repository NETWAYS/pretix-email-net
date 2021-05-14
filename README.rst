NES Mail
==========================

This is a plugin for `pretix`_. 


Clone this repository

`pip3 install <repository>`

Move the NES.html file into the pretix templates folder, located under $Pythonpath/pretix/base/templates/pretixbase/email/ and name it NES.html

migrate and rebuild Pretix with `python3 -m pretix migrate` and `python3 -m pretix rebuild` 
restart the server 

Enable the Plugin in the Plugin Selection, under Customization


