from django.db import models
from time import time
from datetime import date

def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)

class Article(models.Model):
	Title = models.CharField(max_length=200)
	Date = models.DateField()
	Author = models.CharField(max_length=50)
	Text = models.TextField()
	Image = models.FileField(upload_to=get_upload_file_name)

	def __unicode__(self):
		return self.Title