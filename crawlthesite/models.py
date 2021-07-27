from django.db import models

# Create your models here.
class SanctionsList(models.Model):
    Type = models.CharField(max_length=100, default='All')
    Address = models.CharField(max_length=250, null=True, blank=True)
    Name = models.CharField(max_length=250)
    City = models.CharField(max_length=100, null=True, blank=True)
    ID_Field = models.CharField(max_length=100, null=True, blank=True)
    State = models.CharField(max_length=100, null=True, blank=True)
    Program = models.CharField(max_length=50, default='All', blank=True)
    Country = models.CharField(max_length=100, default='All')
    MinNameScore = models.SmallIntegerField()
    List = models.CharField(max_length=250, default='All')

    def __str__(self):
        return self.Name
