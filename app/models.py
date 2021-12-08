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


class Experience(models.Model):
    occupation = models.CharField('occupation', max_length=100)
    company = models.CharField('company', max_length=100)
    description = models.TextField('explanation')
    place = models.CharField('place', max_length=100)
    period = models.CharField('period', max_length=100)
    
    def __str__(self):
        return self.occupation


class Education(models.Model):
    course = models.CharField('course', max_length=100)
    school = models.CharField('school', max_length=100)
    place = models.CharField('place', max_length=100)
    period = models.CharField('period', max_length=100)

    def __str__(self):
        return self.course


class Software(models.Model):
    name = models.CharField('Software', max_length=100)
    level = models.CharField('Level', max_length=100)
    percentage = models.IntegerField('Percentage')
    
    def __str__(self):
        return self.name


class Technical(models.Model):
    name = models.CharField('Technical', max_length=100)
    level = models.CharField('Level', max_length=100)
    percentage = models.IntegerField('Percentage')

    def __str__(self):
        return self.name