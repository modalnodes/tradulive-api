from django.contrib import admin

from .models import *

admin.site.register(Language)
admin.site.register(LanguageLevel)
admin.site.register(CertificationLevel)
admin.site.register(PersonTitle)
admin.site.register(CertificationIssuer)
admin.site.register(MicroVocabulary)
admin.site.register(Certification)
admin.site.register(TranslatorProfile)
admin.site.register(TranslatorLanguage)
admin.site.register(TranslatorMicrovoc)
admin.site.register(TranslatorMode)
admin.site.register(CustomerProfile)
admin.site.register(CustomerUser)
admin.site.register(CreditAssignment)
admin.site.register(Transaction)
admin.site.register(Appointment)
admin.site.register(AppointmentClosure)
admin.site.register(AppointmentEvaluation)
admin.site.register(TranslatorInvoice)