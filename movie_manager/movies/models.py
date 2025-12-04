from django.db import models

# Create your models here.


class CensorInfo(models.Model):
    rating=models.CharField(max_length=10,null=True)
    cirtified_by=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.cirtified_by
        

    


class Directors(models.Model):
    name=models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Actors(models.Model):
    name=models.CharField(max_length=250)



class MovieInfo(models.Model):
    title=models.CharField(max_length=90)
    year=models.IntegerField(null=True)
    description=models.TextField()
    poster=models.ImageField(upload_to='images/',null=True)
    censor_details=models.OneToOneField(CensorInfo,on_delete=models.SET_NULL,related_name='movies',null=True)
    directed_by=models.ForeignKey(Directors,null=True,on_delete=models.CASCADE,related_name='directed_movies')
    actors=models.ManyToManyField(Actors,related_name='acted_movies')

    

    def __str__(self):
        return self.title


