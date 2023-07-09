from django.db import models

# Create your models here.
class SocialLink(models.Model):
    # Define your fields here
    # For example:
    title = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.title
    
class About(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title    