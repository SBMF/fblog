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


# I based this off of a snip I found @ http://snipt.net/patrickbeeson/django-blog-entry-model
# One major adjustment is the way we will handle tags, basing the system off serious-internte.biz, we will hvave 
# static tags in the model - you may think this is crazy, but it works really well, especially when crowd sourced
# moderation can change the tags based on the information it allows for much more precise data cataloging. 
# ...
# when combined with tonnes of caching care-of-memcached this method is not expensive at all and is very easy to manage.

class Entry(models.Model):
	# Status options
	CLOSED_STATUS = 1
	EDITING_STATUS = 2
	LIVE_STATUS = 3
	STATUS_CHOICES = (
		(CLOSED_STATUS, 'Closed'),
		(EDITING_STATUS, 'Editing'),
		(LIVE_STATUS, 'Public'),
	)


	# Title and slug fields
	title = models.CharField(max_length=200, help_text='This field will populate the slug field. Maximum 200 characters.')
	slug = models.SlugField(unique_for_date='pub_date')
	
	# Summary and body fields
	summary = models.TextField(help_text='Summary of post')
	body = models.TextField(help_text='Blog Entry')

	# Tag fields
	tag1 = models.CharField(max_length=20, blank=True, null=True) 
	tag2 = models.CharField(max_length=20, blank=True, null=True) 
	tag3 = models.CharField(max_length=20, blank=True, null=True) 
	tag4 = models.CharField(max_length=20, blank=True, null=True) 
	
	# Meta fields
	meta_keywords = models.CharField(blank=True, max_length=300, help_text='Comma-separated list of keyworks for this entry. Maximum 300 characters.')
	meta_description = models.CharField(blank=True, max_length=400, help_text='A brief description of this entry. Maximum 400 characters.')
	
	# Image field - not yet!  will configure this once the media section is working
	# centerpiece_image = models.ForeignKey(Photo, blank=True, null=True)
	
	# Date fields
	pub_date = models.DateTimeField(default=datetime.datetime.now)
	cal_date = models.DateTimeField(blank=True, auto_now=False, null=Tre) # this will allow us to add blog entries to the calendar before .datetime.now
	update = models.DateTimeField(blank=True, editable=True, auto_now=False, null=True)
	
	# Author field
	author = models.ForeignKey(User)
	
	# Enable comments field
	enable_comments = models.BooleanField(default=True)
	
	# Entry status field
	status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=EDITING_STATUS)
	
	def __unicode__(self):
		return self.title
