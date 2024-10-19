from django.db import models

# Create your models here.

class About(models.Model):
    about_heading = models.CharField(max_length=30)
    about_desc = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.about_heading


class Sociallink(models.Model):
    platform = models.CharField(max_length=30)
    link  = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.platform