from django.db import models
#import user class
from django.contrib.auth import get_user_model
# Create your models here.
class Snack(models.Model):
     name = models.CharField(max_length= 64)
     #ForeignKey is away to associate a record from one model with arecord from another model
     
     purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
     #Notes: Cascade Delete option means that if a record from one table is deleted,..
     #corresponding records in the other table are also deleted.
     description = models.TextField(max_length= 800)


     def __str__(self):
        return self.name