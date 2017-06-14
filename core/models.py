from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
        
class LanguageLevel(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    

class TranslatorProfile(models.Model):
    user = models.ForeignKey(User)
    
class TranslatorLanguage(models.Model):
    translator = models.ForeignKey(TranslatorProfile, related_name="languages")
    language = models.ForeignKey(Language, related_name="translators")
    level = models.ForeignKey(LanguageLevel, related_name="translators")
    