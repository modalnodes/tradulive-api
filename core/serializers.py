from rest_framework import serializers

from .models import * 

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"
        
class LanguageLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageLevel
        fields = "__all__"
        
class CertificationLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificationLevel
        fields = "__all__"
        
class PersonTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonTitle
        fields = "__all__"
        
class CertificationIssuerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificationIssuer
        fields = "__all__"
        
class MicroVocabularySerializer(serializers.ModelSerializer):
    class Meta:
        model = MicroVocabulary
        fields = "__all__"
        
class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = "__all__"
        
class TranslatorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslatorProfile
        fields = "__all__"
        
class TranslatorLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslatorLanguage
        fields = "__all__"
        
class TranslatorMicrovocSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslatorMicrovoc
        fields = "__all__"
        
class TranslatorModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslatorMode
        fields = "__all__"
        
class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = "__all__"
        
class CustomerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = "__all__"
        
class CreditAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditAssignment
        fields = "__all__"
        
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"
        
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"
        
class AppointmentClosureSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentClosure
        fields = "__all__"
        
class AppointmentEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentEvaluation
        fields = "__all__"
        
class TranslatorInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslatorInvoice
        fields = "__all__"
        