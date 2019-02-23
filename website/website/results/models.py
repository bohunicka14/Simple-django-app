from django.db import models

class Result(models.Model):

	id = models.IntegerField(primary_key=True)
	value = models.IntegerField()
	idGame = models.PositiveSmallIntegerField()
	idUser = models.IntegerField()
	date = models.DateTimeField()
	
