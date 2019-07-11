from django.db import models
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date publishied')
    body = models.TextField()
    
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Comment(models.Model):
    comment = models.CharField(max_length=200)

    def __str__(self):
        return self.comment

    def summary(self):
        return self.comment
# Create your models here.
