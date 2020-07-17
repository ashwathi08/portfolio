from django.db import models

# Create your models here.
class About(models.Model):
    short_desp=models.TextField()
    desp=models.TextField()
    image=models.ImageField(upload_to='images/')

    class Meta:
        verbose_name="About Me"

    def __str__(self):
        return "About me"

class Skills(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='skill/')

    def __str__(self):
        return self.title