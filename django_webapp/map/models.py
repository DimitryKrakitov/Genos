from django.db import models

# Create your models here.

class Campus(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Building(models.Model):
    name = models.CharField(max_length=200)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " - " + self.campus.name

class Floor(models.Model):
    name = models.CharField(max_length=200)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " - " + self.building.name + " - " + self.building.campus.name

class Room(models.Model):
    name = models.CharField(max_length=200)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " - " + self.floor.name + " - " + self.floor.building.name + " - " + self.floor.building.campus.name
