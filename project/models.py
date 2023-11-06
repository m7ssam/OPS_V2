from django.db import models

# Create your models here.

class Name(models.Model):
  recipient = models.CharField(max_length=6, primary_key=True)
  project_name = models.CharField(max_length=50)
  def __str__(self):
      return self.project_name

class Photo(models.Model):
  recipient = models.ForeignKey("Name.recipient", on_delete=models.CASCADE)
  photo = models.models.ImageField(upload_to = f'media/project/{recipient}', default = "static\images\Project\Cover\default.jpg")
  def __str__(self):
      return self.recipient