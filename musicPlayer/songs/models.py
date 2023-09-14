from django.db import models

# Create your models here.
class Songs(models.Model):
	title=models.TextField()
	artist=models.TextField()
	image=models.ImageField()
	audio_file = models.FileField(blank=True,null=True)

	def __str__(self):
	        return self.title
