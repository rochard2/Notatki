from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Note(models.Model):
    # menadzery obiketow
    objects = models.Manager()
    published = PublishedManager()

    title = models.CharField(max_length=250)
    body = models.TextField()

    PRIORITY_CHOICES = (
        ('1_high', "Bardzo ważne"),
        ('2_medium', "Średnio ważne"),
        ('3_low', "Mało ważne")
    )

    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES,
                                default='medium')

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Opublikowany')
    )

    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='published')

    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notatki:note_detail', args=[self.publish.year,
                                                    self.publish.month,
                                                    self.publish.day,
                                                    self.slug])

    class Meta:
        ordering = ('created',)
