from django.db import models


# Create your models here.


class HelpTickets(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=600)

    # TODO implement more such as files, or Image to be sent regarding the problem
