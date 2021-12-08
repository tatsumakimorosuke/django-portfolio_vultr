from django.db import models


class Profile(models.Model):
    title = models.CharField('Title',max_length=100, null=True, blank=True)
    subtitle = models.CharField('Subtitle',max_length=100, null=True, blank=True)
    name = models.CharField('Name',max_length=100)
    job = models.TextField('Job')
    introduction = models.TextField('Introduction')
    github = models.CharField('github',max_length=100, null=True, blank=True)
    twitter = models.CharField('twitter',max_length=100, null=True, blank=True)
    linkedin = models.CharField('linkedin',max_length=100, null=True, blank=True)
    facebook = models.CharField('facebook',max_length=100, null=True, blank=True)
    instagram = models.CharField('instagram',max_length=100, null=True, blank=True)
    topimage = models.ImageField(upload_to='images', verbose_name='TopImages')
    subimage = models.ImageField(upload_to='images', verbose_name='SubImages')

def __str__(self):
    return self.name


class Work(models.Model):
    title = models.CharField('title', max_length=100)
    image = models.ImageField(upload_to='images', verbose_name='images')
    thumbnail = models.ImageField(upload_to='images', verbose_name='thumbnail', null=True, blank=True)
    skill = models.CharField('skill', max_length=100)
    url = models.CharField('url', max_length=100, null=True, blank=True)
    created = models.DateField('Created date')
    description = models.TextField('explanation')

    def __str__(self):
        return self.title