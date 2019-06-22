from django.db import models

# blog posts from; both admin and users

class Blog(models.Model):

    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return self.title

    def thumbnail(self):
        return self.body[:20]

class Guest(models.Model):

    title = models.CharField(max_length=50, default="은정리 hi")
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=500)


    def __str__(self):
        return self.title

    def thumbnail(self):
        return self.body[:10]


    
 
