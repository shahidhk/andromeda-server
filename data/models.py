from django.db import models

class Kadai(models.Model):
    name            = models.CharField(max_length=100)
    description     = models.TextField(blank=True, null=True)
    image           = models.ImageField(upload_to="pics", blank=True, null=True)

    def __unicode__(self):
        return self.name
