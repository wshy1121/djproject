from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    def __unicode__(self):
        return self.name
			
    def my_property(self):
        return self.name + ' ' + ' is a person'
    my_property.short_description = "Full name of the person"
    
    full_name = property(my_property)    

