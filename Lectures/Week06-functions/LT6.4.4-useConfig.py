# uses config to show how you would use a configuration file

import config as cfg


# this takes gmail out of the config.py program and you pass in the 'password' then
password = cfg.gmail['password']

print (password)

