from django.db import models


from django.db import models

class Praise(models.Model):
    praised_to = models.CharField(max_length=100)
    praised_by = models.CharField(max_length=100)
    praise_text = models.TextField()
    image = models.ImageField(upload_to='praise_images/')
    badge_icon = models.ImageField(upload_to='badge_icons/')

    def __str__(self):
        return self.praised_to


