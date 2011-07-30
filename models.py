# Welcome to FBlog! its called FBlog because FutureBlog sounds bad. 
# The models in this file will allow us to enter data at any time along 
# a timeline and present it in the views.py in a blogging format.
# e.g.: 
# you could make a retro-active blog for a day you remember long ago.
# you could make a blog entry for an upcoming event and keep notes on it
# .....
# we are going to use this system to set milestones for the project and keep 
# a log of its development. 
# -- Greg 

from django.db import models
from django.contrib.auth.models import User

class BlogEntry(models.Model):
    blog_by = models.ForeignKey(User)
