from django.db import models

# Create your models here.

'''
CREATE TABLE Person (
    "id" serial NOT NULL PRIMARY KEY,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL
)

This is equvalent to under this code 



class Person(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
'''


class Musician(models.Model):
    # id = models.AutoField(primary_key=True) # automatically declare if there no primary key
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    # this function is for showing data in Object
    def __str__(self):
        return self.first_name + " " + self.last_name


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    # CASCADE: if any Musician delete, then here his Album automatcally delete
    name = models.CharField(max_length=100)
    release_date = models.DateField()

    rating = (
        (1, "Worst"),
        (2, "Bad"),
        (3, "Not Bad"),
        (4, "Good"),
        (5, "Excellent!"),
    )

    num_stars = models.IntegerField(choices=rating)

    def __str__(self):
        return self.name + ", Rating: " + str(self.num_stars)
