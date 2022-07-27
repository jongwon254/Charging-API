from django.db import models

# Database model
class ChargingPoint(models.Model):
    operator = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    house_number = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    power = models.DecimalField(max_digits=5, decimal_places=2)
    number_ports = models.IntegerField()

    def __str__(self):
        return self.operator + ' in ' + self.city
