from django.db import models

# Create your models here.
class EasyLevel(models.Model):
    Participant_Name = models.CharField(max_length=50)
    Submission_Time = models.DateTimeField()
    Score = models.IntegerField()

class MediumLevel(models.Model):
    Participant_Name = models.CharField(max_length=50)
    Submission_Time = models.DateTimeField()
    Score = models.IntegerField()

class HardLevel(models.Model):
    Participant_Name = models.CharField(max_length=50)
    Submission_Time = models.DateTimeField()
    Score = models.IntegerField()


