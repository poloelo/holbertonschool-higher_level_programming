#!/bin/usr/python

class User : 
    name = ""
    nombreuser = 0

class Paul(User):
    def __init__(self):
        super().nombreuser += 1
        
print(User.nombreuser)