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

# creating 'photos' posts; only from admin, not from users (form not needed)

class Photo(models.Model):
    title = models.CharField(max_length=200, default='untitled')
    image = models.ImageField()
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    def thumbnail(self):
        return self.image
    
 
