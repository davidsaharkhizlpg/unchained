from django.db import models

# Create your models here.

#extend class model to create a poll
#create two field classes of type models.Charfield()
class Poll(models.Model):
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	
class Choice(models.Model) :
	#establishes a many-to-one relationship, each choice is associated with a foreign key poll
	poll = models.ForeignKey(Poll)
	choice = models.CharField(max_length=200)
	votes = models.IntegerField()