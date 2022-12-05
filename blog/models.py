from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=10)
    description = models.TextField()
    date = models.DateField(blank=True,null=True)

    def __str__(self):
        #文字列にした時に、どんな表示にするか
        return self.title
