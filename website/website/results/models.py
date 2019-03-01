from django.db import models


class Games(models.Model):

	id = models.IntegerField(primary_key=True)
	name = models.TextField()

	class Meta:
		db_table = "games"

class Auth_user(models.Model):

	id = models.IntegerField(primary_key=True)
	username = models.TextField()

	class Meta:
		db_table = "auth_user"

class Result(models.Model):

	id = models.IntegerField(primary_key=True)
	value = models.IntegerField()
	game = models.ForeignKey('Games', on_delete = models.CASCADE)
	user = models.ForeignKey('Auth_user', on_delete = models.CASCADE)
	date = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = "results"
	




