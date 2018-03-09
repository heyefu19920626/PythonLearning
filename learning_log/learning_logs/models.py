from django.db import models

# Create your models here.

class Topic(models.Model):
    """ the subject of user learning """
    text = models.CharField(max_length=200)
    date_added = models.DataTimeField(auto_now_add=True)

    def __str__(self):
        """ return the string representation of the model """
        return self.text