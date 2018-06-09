from django.db import models
from time import time
from datetime import date

def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)

class Robot(models.Model):
	Name = models.CharField(max_length=200)
	Date = models.DateField()
	Thumb = models.FileField(upload_to=get_upload_file_name)
	Image = models.FileField(upload_to=get_upload_file_name)
	TinyMCE = models.TextField()
	Kit = models.FileField(upload_to=get_upload_file_name)
	Software = models.FileField(upload_to=get_upload_file_name)

	def __unicode__(self):
		return self.Name
