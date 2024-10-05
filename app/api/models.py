from django.db import models

# Информацию о моделях можно узнать в /docs/models.md   

class Title(models.Model):
    name = models.TextField()
    link = models.TextField()

class Chapter(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    name = models.TextField()
    status = models.BooleanField()
    original = models.TextField()

class Worker(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    nickname = models.TextField()
    contact = models.TextField()
    occupation = models.TextField()