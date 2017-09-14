from rest_framework import viewsets

from .models import * 

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class=LanguageSerializer
    
class LanguageLevelViewSet(viewsets.ModelViewSet):
    queryset = LanguageLevel.objects.all()
    serializer_class=LanguageLevelSerializer
    
class CertificationLevelViewSet(viewsets.ModelViewSet):
    queryset = CertificationLevel.objects.all()
    serializer_class=CertificationLevelSerializer
    
class PersonTitleViewSet(viewsets.ModelViewSet):
    queryset = PersonTitle.objects.all()
    serializer_class=PersonTitleSerializer
    
class CertificationIssuerViewSet(viewsets.ModelViewSet):
    queryset = CertificationIssuer.objects.all()
    serializer_class=CertificationIssuerSerializer
    
class MicroVocabularyViewSet(viewsets.ModelViewSet):
    queryset = MicroVocabulary.objects.all()
    serializer_class=MicroVocabularySerializer
    
class CertificationViewSet(viewsets.ModelViewSet):
    queryset = Certification.objects.all()
    serializer_class=CertificationSerializer
    
class TranslatorProfileViewSet(viewsets.ModelViewSet):
    queryset = TranslatorProfile.objects.all()
    serializer_class=TranslatorProfileSerializer
    
class TranslatorLanguageViewSet(viewsets.ModelViewSet):
    queryset = TranslatorLanguage.objects.all()
    serializer_class=TranslatorLanguageSerializer
    
class TranslatorMicrovocViewSet(viewsets.ModelViewSet):
    queryset = TranslatorMicrovoc.objects.all()
    serializer_class=TranslatorMicrovocSerializer
    
class TranslatorModeViewSet(viewsets.ModelViewSet):
    queryset = TranslatorMode.objects.all()
    serializer_class=TranslatorModeSerializer
    
class CustomerProfileViewSet(viewsets.ModelViewSet):
    queryset = CustomerProfile.objects.all()
    serializer_class=CustomerProfileSerializer
    
class CustomerUserViewSet(viewsets.ModelViewSet):
    queryset = CustomerUser.objects.all()
    serializer_class=CustomerUserSerializer
    
class CreditAssignmentViewSet(viewsets.ModelViewSet):
    queryset = CreditAssignment.objects.all()
    serializer_class=CreditAssignmentSerializer
    
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class=TransactionSerializer
    
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class=AppointmentSerializer
    
class AppointmentClosureViewSet(viewsets.ModelViewSet):
    queryset = AppointmentClosure.objects.all()
    serializer_class=AppointmentClosureSerializer
    
class AppointmentEvaluationViewSet(viewsets.ModelViewSet):
    queryset = AppointmentEvaluation.objects.all()
    serializer_class=AppointmentEvaluationSerializer
    
class TranslatorInvoiceViewSet(viewsets.ModelViewSet):
    queryset = TranslatorInvoice.objects.all()
    serializer_class=TranslatorInvoiceSerializer
    