from django.db import models


class Games(models.Model):

	id = models.IntegerField(primary_key=True)
	name = models.TextField()

class Auth_user(models.Model):

	id = models.IntegerField(primary_key=True)
	username = models.TextField()

class Result(models.Model):

	id = models.IntegerField(primary_key=True)
	value = models.IntegerField()
	game = models.ForeignKey('Games', on_delete = models.CASCADE)
	user = models.ForeignKey('Auth_user', on_delete = models.CASCADE)
	date = models.DateTimeField()
	




