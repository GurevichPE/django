from django.db import models

# Create your models here.
class Nematoda(models.Model):
    name = models.CharField(max_length=16)
    length = models.FloatField(default=1)

    def __str__(self):
        return str(self.id) + ': ' + str(self.name) + ' длина: ' + str(self.length)

class TypesOfWorm(models.Model):

    name = models.CharField(max_length=16)
    def __str__(self):
        return self.name

class SubTypesOfWorm(models.Model):

    name = models.CharField(max_length=16)
    def __str__(self):
        return self.name

class Worm(models.Model):
    type = models.ForeignKey(TypesOfWorm, null=True, blank=True, on_delete=models.CASCADE)
    sub_type = models.ManyToManyField(SubTypesOfWorm, null=True, blank=True)
    name = models.CharField(max_length=16)
    exp_name = models.CharField(max_length=16)
    def __str__(self):
        return self.name

class ParametrsWorm(models.Model):
    worm = models.OneToOneField(Worm, on_delete=models.CASCADE)
    length = models.FloatField(default=1)
    height = models.FloatField(default=1)
    def __str__(self):
        return str(self.worm)