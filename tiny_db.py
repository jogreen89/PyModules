"""TinyDB script"""
#!/usr/bin/python

# Imports
from tinydb import TinyDB
# Print a message to console
print("Hello TinyDB.")
db = TinyDB('db.json')
db.insert({'type': 'apple', 'count': 7})
db.insert({'type': 'peach', 'count': 3})
db.all()
