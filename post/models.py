from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from .managers import PublishedManager
from django.urls import reverse


class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(Base):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f" Category: {self.name}"

    class Meta:
        ordering = ['-updated']
        indexes = [models.Index(fields=['-updated'])]

    def get_absolute_url(self):
        return reverse('post:post_by_category', args=[self.pk])


class Post(Base):
    class Status(models.TextChoices):
        DRAFT = 'DR', 'draft'
        PUBLISH = 'PB', 'publish'

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, unique_for_date='created')
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    categories = models.ManyToManyField(Category, related_name='posts', blank=True)
    tags = TaggableManager()
    status = models.CharField(max_length=2, default=Status.DRAFT, choices=Status.choices)
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-updated']
        indexes = [models.Index(fields=['-updated'])]


class Image(Base):
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f"{self.post.title}'s images"

    class Meta:
        ordering = ['-updated']
        indexes = [models.Index(fields=['-updated'])]


class Comment(Base):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-updated']
        indexes = [models.Index(fields=['-updated'])]


class About(Base):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title
