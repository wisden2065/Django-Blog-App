from django.db import models

from django.utils import timezone

# python creates a table with authentication 
from  django.contrib.auth.models import User

# Create your models here.
# Models helps us to interact with database directly by reading or writing to the database
# the data will be sent back to the views


# we a creating a class that would be inheriting from the models Module
class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default = timezone.now())
    created  = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    # foreign key lets us link tables with tables---in this case points to the User
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "blog_app") 

    # ref (foreign key)----one to many
    # primary key uniquely identifies a table eg ID


# Defining a sort order
    class Meta:
        ordering = ['-publish']


# String readable attr 
    def __str__(self):
        return self.title
    
