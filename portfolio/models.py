from django.db import models

class Photo(models.Model):

    title = models.CharField(max_length=50, default="untitled")
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/",  default="none")

    def __str__(self):
        return self.title

    def thumbnail(self):
        return self.image

