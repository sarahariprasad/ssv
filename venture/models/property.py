from django.db import models
# Create your models here.

availability_type = (
    ('for sale', 'for sale'),
    ('sold out', 'sold out')
)


class Property(models.Model):
    name = models.CharField(max_length=50)
    availability = models.CharField(choices=availability_type, max_length=50, default='')
    location = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='property/', null=True)

    def __str__(self):
        return self.name



