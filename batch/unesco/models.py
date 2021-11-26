from django.db import models

# name	description	justification	year	longitude	latitude	area_hectares	category	state	region	iso


class Category(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=128)
    
    def __str__(self):
        return self.name
        
class Iso(models.Model):
    name = models.CharField(max_length=128)
      
    def __str__(self):
        return self.name


class State(models.Model) :
    name = models.CharField(max_length=128)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    iso = models.ForeignKey(Iso, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Site(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField(null=True)
    iso = models.ForeignKey(Iso, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    justification = models.TextField()
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    area_hectares = models.FloatField(null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    

    def __str__(self) :
        return self.name
