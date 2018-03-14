from django.db import models
from django.utils import timezone


class producer(models.Model):
    name=models.TextField()
    address=models.TextField()
    dateofbirth=models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.name

class production(models.Model):
    options=(('first','First'),('second','Second'),('third', 'Third'),('fourth','Fourth'))
    year=models.CharField(max_length=4)
    quarter=models.CharField(max_length=1,choices=options)
    producer=models.ForeignKey(producer)

