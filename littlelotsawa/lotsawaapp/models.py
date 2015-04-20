from django.db import models
from django.contrib.auth.models import AbstractUser

class Interests(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Skills(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class MyUser(AbstractUser):
    skype = models.CharField(max_length=80, blank=True, null=True)
    skill = models.ForeignKey(Skills, blank=True, null=True)
    interests = models.ManyToManyField(Interests, blank=True, null=True)
    searching = models.BooleanField(default=False)

    @classmethod
    def getbyskill(cls, skill):
        users = MyUser.object.filter(skill = skill)
        return users

    @classmethod
    def getbyinterest(cls, interests):
        users = MyUser.object.filter(interests = interests)
        return users

    def show_trainingpartners(self):
        return list(MyUser.objects.filter(searching = True, skill = self.skill).exclude(username = self.username))

class Region(models.Model):
    name = models.CharField(max_length=120)
    shortdescription = models.CharField(max_length=400)
    superregion = models.ForeignKey('self', blank=True, null=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Dialect(models.Model):
    name = models.CharField(max_length=120)
    region = models.ManyToManyField(Region, blank=True, null=True)
    superdialect = models.ForeignKey('self', blank=True, null=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Vocabulary(models.Model):
    tibetan = models.CharField(unique=True,max_length=120)
    english = models.CharField(max_length=120)
    german = models.CharField(max_length=120, blank=True, null=True)
    pronounciation = models.CharField(max_length=120)
    dialect = models.ForeignKey(Dialect, blank=True, null=True)
    categories = models.ManyToManyField(Topic, blank=True, null=True)
    notes = models.CharField(max_length=400, blank=True, null=True)
    validated = models.BooleanField(default=False)

    def __str__(self):              # __unicode__ on Python 2
        return self.tibetan

class VocabularyValidation(models.Model):
    word = models.ForeignKey(Vocabulary, unique=True)
    validated_by = models.ManyToManyField(MyUser, blank=True, null=True)
    count = models.IntegerField(default=0)
    validationborder = models.IntegerField(default=10)

    def __str__(self):              # __unicode__ on Python 2
        return self.word.tibetan + "-validation"
