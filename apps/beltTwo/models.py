from __future__ import unicode_literals
from django.db import models
from ..loginReg.models import User

class QManager(models.Manager):
	def validate(self, data):
		flag = True
		errors = []
		if len(data['by']) < 3:
			flag = False
			errors.append('Quoted By must be greater than 3 characters')
		if len(data['message']) < 10:
			flag = False
			errors.append('Messages must be greater than 3 characters')
		if flag:
			quote = Quotes.objects.create(quote=data['message'], by=data['by'], user=data['user'])
			return (True, quote)
		else:
			return (False, errors)

class Quotes(models.Model):
	quote = models.CharField(max_length = 255)
	by = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	user = models.ForeignKey(User, related_name="posted_quotes")
	objects = QManager()

class Favorites(models.Model):
	quotes = models.ForeignKey(Quotes, related_name="favs")
	user = models.ForeignKey(User, related_name="all_users")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)


