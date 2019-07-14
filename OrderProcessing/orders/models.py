from django.db import models

# Create your models here.
class Order(models.Model):
	description = models.TextField(verbose_name='Description', max_length=512)
	price = models.IntegerField(verbose_name='Price', db_index=True)
