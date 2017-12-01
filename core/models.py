from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models import Sum

from timezone_field import TimeZoneField
# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=4)
    def __str__(self):
        return self.name
        
class LanguageLevel(models.Model):
    name = models.CharField(max_length=200)
    credit_multiplier = models.FloatField()
    def __str__(self):
        return self.name
        
class CertificationLevel(models.Model):
    name = models.CharField(max_length=200)
    value = models.IntegerField()
    
    def __str__(self):
        return self.name
        
    class Meta:
        ordering=["value"]
        
class PersonTitle(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
        
class CertificationIssuer(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class MicroVocabulary(models.Model):
    icon = models.URLField(null=True, blank=True)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Certification(models.Model):
    name = models.CharField(max_length=200)
    issuer = models.ForeignKey(CertificationIssuer)
    level = models.ForeignKey(CertificationLevel)
    language_from = models.ForeignKey(Language, related_name="certified_from")
    language_to = models.ForeignKey(Language, related_name="certified_to")
    def __str__(self):
        return self.name

class TelModel(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="AA Telephone Model"

class ComputerModel(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="AA Computer Model"

class TabletModel(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="AA Tablet Model"

class CableInternet(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="AA Cable Internet"

class CableInternetProvider(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="AA Cable Internet Provider"

class MobileInternet(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="AA Mobile Internet"

class MobileInternetProvider(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="AA Mobile Internet Provider"


class TranslatorProfile(models.Model):
    user = models.ForeignKey(User)
    tel_home = models.CharField(max_length=200, null=True, blank=True)
    tel_office = models.CharField(max_length=200, null=True, blank=True)
    tel_private_cell = models.CharField(max_length=200, null=True, blank=True)
    tel_work_cell = models.CharField(max_length=200, null=True, blank=True)
    fax = models.CharField(max_length=200, null=True, blank=True)
    skype = models.CharField(max_length=200, null=True, blank=True)
    secondary_mail = models.CharField(max_length=200, null=True, blank=True)
    tel_model = models.CharField(max_length=200, null=True, blank=True)
    computer_model = models.CharField(max_length=200, null=True, blank=True)
    tablet_model = models.CharField(max_length=200, null=True, blank=True)
    cable_internet = models.CharField(max_length=200, null=True, blank=True)
    cable_internet_provider = models.CharField(max_length=200, null=True, blank=True)
    mobile_internet = models.CharField(max_length=200, null=True, blank=True)
    mobile_internet_provider = models.CharField(max_length=200, null=True, blank=True)
    birth_day = models.DateField(null=True, blank=True)
    birth_city = models.CharField(max_length=200, null=True, blank=True)
    birth_country = models.CharField(max_length=200, null=True, blank=True)
    native_lang_1 = models.ForeignKey(Language, related_name="natives")
    native_lang_2 = models.ForeignKey(Language, null=True, blank=True, related_name="secondary_natives")
    Nationality = models.CharField(max_length=200, null=True, blank=True)
    home_address = models.CharField(max_length=200, null=True, blank=True)
    home_city = models.CharField(max_length=200, null=True, blank=True)
    home_country = models.CharField(max_length=200, null=True, blank=True)
    title = models.ForeignKey(PersonTitle, null=True, blank=True)
    timezone = TimeZoneField(null=True, blank=True)
    vat_num = models.CharField(max_length=200, null=True, blank=True)
    soc_num = models.CharField(max_length=200, null=True, blank=True)
    bank = models.CharField(max_length=200, null=True, blank=True)
    iban = models.CharField(max_length=200, null=True, blank=True)
    swift = models.CharField(max_length=200, null=True, blank=True)
    paypal = models.CharField(max_length=200, null=True, blank=True)
    picture = models.URLField(null=True, blank=True)
    video_pres = models.URLField(null=True, blank=True)
    id_card = models.URLField(null=True, blank=True)
    passport = models.URLField(null=True, blank=True)
    vat_pic = models.URLField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.user.username
    
class TranslatorLanguage(models.Model):
    translator = models.ForeignKey(TranslatorProfile, related_name="languages")
    language_from = models.ForeignKey(Language, related_name="translate_to")
    language_to = models.ForeignKey(Language, related_name="translate_from")
    level = models.ForeignKey(LanguageLevel, related_name="translators")
    certification = models.ForeignKey(Certification)
    certification_code = models.CharField(max_length=200, null=True, blank=True)
    date_reached = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return "{} - {}->{}:{} ({}:{})".format(self.translator, self.language_from, self.language_to, self.level, self.certification, self.certification_code)

class TranslatorMicrovoc(models.Model):
    translator = models.ForeignKey(TranslatorProfile, related_name="microvocs")
    language_from = models.ForeignKey(Language, related_name="microvoc_to")
    language_to = models.ForeignKey(Language, related_name="microvoc_from")
    lang = models.ForeignKey(TranslatorLanguage, related_name="microvoc", null=True)
    microvoc = models.ForeignKey(MicroVocabulary, related_name="languages")
    amount = models.IntegerField()
    
    def __str__(self):
        return "{} - {}->{}:{}={}".format(self.translator, self.language_from, self.language_to, self.microvoc, self.amount)
    
class TranslatorMode(models.Model):
    translator = models.ForeignKey(TranslatorProfile, related_name="modes")
    from_language = models.ForeignKey(Language, related_name="froms")
    to_language = models.ForeignKey(Language, related_name="toes")
    lang = models.ForeignKey(TranslatorLanguage, related_name="mode", null=True)
    passive_translator = models.BooleanField(default=True)
    
    def __str__(self):
        return "{} - {}:{}".format(self.translator, self.lang, "passive" if self.passive_translator else "active")
    

class CustomerProfile(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, related_name="profile")
    group = models.ForeignKey(Group)
    parent = models.ForeignKey('CustomerProfile', null=True, blank=True)
    
    address = models.TextField()
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    vat_number = models.CharField(max_length=200)
    tel = models.CharField(max_length=200)
    fax = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    website = models.URLField()
    notes = models.TextField()
    
    
    tel_home = models.CharField(max_length=200, null=True, blank=True)
    tel_office = models.CharField(max_length=200, null=True, blank=True)
    tel_private_cell = models.CharField(max_length=200, null=True, blank=True)
    tel_work_cell = models.CharField(max_length=200, null=True, blank=True)
    fax = models.CharField(max_length=200, null=True, blank=True)
    skype = models.CharField(max_length=200, null=True, blank=True)
    secondary_mail = models.CharField(max_length=200, null=True, blank=True)
    
    home_address = models.CharField(max_length=200, null=True, blank=True)
    home_city = models.CharField(max_length=200, null=True, blank=True)
    home_country = models.CharField(max_length=200, null=True, blank=True)
    title = models.ForeignKey(PersonTitle, null=True, blank=True)
    timezone = TimeZoneField(null=True, blank=True)

    def minutes(self):
        return self.transactions.all().aggregate(Sum("value"))["value__sum"]
        
    def __str__(self):
        return "{} - {}::{} ({})".format(self.name, self.group, self.owner, self.minutes())
    


class CustomerUser(models.Model):
    customer = models.ForeignKey(CustomerProfile, related_name="users")
    user = models.ForeignKey(User)
    
    tel_home = models.CharField(max_length=200)
    tel_office = models.CharField(max_length=200)
    
    def __str__(self):
        return "{}, {}".format(self.user, self.customer)
    
class Transaction(models.Model):
    customer = models.ForeignKey(CustomerProfile, related_name="transactions")
    author = models.ForeignKey(CustomerUser)
    created = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    value = models.FloatField(default=0)
    
    def __str__(self):
        return "{0}:{1} - {2}@{3}".format(self.customer, self.author, self.created, self.amount)
    
class CreditAssignment(models.Model):
    customer = models.ForeignKey(CustomerProfile, related_name="assignments")
    user = models.ForeignKey(User)
    amount = models.IntegerField()
    
    def used_credits(self):
        return self.user.requests.all().aggregate(Sum('credits'))['credits__sum']
    
    def __str__(self):
        return "{}:{} - {} (used: {})".format(self.customer,self.user, self.amount, self.used_credits())
    
class Appointment(models.Model):
    translator = models.ForeignKey(TranslatorProfile, related_name="appointments")
    customer = models.ForeignKey(CustomerProfile, related_name="appointments")
    requester = models.ForeignKey(User, related_name="requests")
    customer_language = models.ForeignKey(Language, related_name="customer_lang_requests")
    other_language = models.ForeignKey(Language, related_name="other_lang_requests")
    level = models.ForeignKey(LanguageLevel)
    microvocs = models.ManyToManyField(MicroVocabulary)
    
    credits = models.IntegerField()
    
    start_ts = models.DateTimeField()
    minutes = models.IntegerField(default=60)
    real_minutes = models.IntegerField(null=True, blank=True)
    url = models.URLField(null=True, blank=True) # generato quando la sesisone inizia
    
    def __str__(self):
        return "{}:{}:{} - {}@{}".format(self.translator, self.customer_language, self.level, self.customer, self.start_ts)
    
class AppointmentClosure(models.Model):
    appointment = models.OneToOneField(Appointment, related_name="closed")
    closer = models.ForeignKey(User)
    closure_reason = models.TextField()
    closure_ts = models.DateTimeField(auto_now_add=True, editable=False)
    notes = models.TextField()

    def __str__(self):
        return "{0}({1}) - {2}@{3}".format(self.appointment, self.appointment.customer, self.closure_reason, self.closure_ts)
    
class AppointmentEvaluation(models.Model):
    appointment = models.ForeignKey(Appointment)
    user = models.ForeignKey(User)
    evaluation = models.IntegerField()
    
    def __str__(self):
        return "{}:{} - {}".format(self.appointment, self.user, self.evaluation)
        
        
class TranslatorInvoice(models.Model):
    translator = models.ForeignKey(TranslatorProfile, related_name="invoices")
    invoice = models.URLField()
    date = models.DateField()
    amount = models.FloatField()
    
    def __str__(self):
        return "{} - Fattura del {} - EUR:{}".format(self.translator, self.date, self.amount)
    
class TranslatorAvailability(models.Model):
    translator = models.ForeignKey(TranslatorProfile, related_name="availabilities")
    dow = models.IntegerField()
    from_time = models.TimeField()
    to_time = models.TimeField()
    created = models.DateTimeField(auto_now=True)
    removed = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return "{} - disponibile il {} dalle {} alle {}".format(self.translator, self.dow, self.from_time, self.to_time)
    class Meta:
        ordering = ["dow"]
    
class TranslatorAvailabilityException(models.Model):
    translator = models.ForeignKey(TranslatorProfile, related_name="exceptions")
    created = models.DateTimeField(auto_now=True)
    removed = models.DateTimeField(null=True, blank=True)
    date_from = models.DateField()
    date_to = models.DateField()
    
    def __str__(self):
        return "{} - non disponibile dal {} al {} ".format(self.translator, self.date_from, self.date_to)
    
    