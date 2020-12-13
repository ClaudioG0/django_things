from django.db import models
from django.contrib.auth.models import User
from django.db.models import Manager

class PublishedManager(Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):

    STATUS_CHOICES = (
        ('Published', 'published'),
        ('Draft', 'draft'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to='main/img/%Y/%m/%d')
    title = models.CharField(max_length=100)
    text = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=40, choices=STATUS_CHOICES)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title



