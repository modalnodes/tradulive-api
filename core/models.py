from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, Group
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
    


class CustomerProfile(models.Model):
    owner = models.ForeignKey(User)
    group = models.ForeignKey(Group)
    
class CustomerUser(models.Model):
    customer = models.ForeignKey(CustomerProfile)
    user = models.ForeignKey(User)
    
class Transaction(models.Model):
    customer = models.ForeignKey(CustomerProfile)
    author = models.ForeignKey(CustomerUser)
    created = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    value = models.FloatField(null=True, blank=True)
    
class Appointment(models.Model):
    translator = models.ForeignKey(TranslatorProfile)
    customer = models.ForeignKey(CustomerProfile)
    language = models.ForeignKey(Language)
    level = models.ForeignKey(LanguageLevel)
    date = models.DateTimeField()
    minutes = models.IntegerField(default=60)
    transaction = models.ForeignKey(Transaction)
    
class AppointmentClosure(models.Model):
    appointment = models.ForeignKey(Appointment)
    transaction = models.ForeignKey(Transaction)
    closure_reason = models.CharField(max_length=200)
    
    