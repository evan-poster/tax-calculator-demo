from django.db import models

# State model for taxes
class State(models.Model):
    # Fields
    name = models.CharField(max_length=100)
    income_tax = models.FloatField()
    property_tax = models.FloatField()

    # Methods
    def __str__(self):
        return self.name

class Town(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    cola_single = models.FloatField()
    cola_four = models.FloatField()

    # Methods
    def __str__(self):
        return self.name


# Personal details
# Starting salary
# Net Income
# Home value
