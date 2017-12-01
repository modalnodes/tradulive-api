from rest_framework import serializers
from django.db.models import Q
from .models import * 
import datetime
        
class AppointmentSerializer(serializers.ModelSerializer):
    start = serializers.SerializerMethodField()
    end = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    
    def get_start(self, obj):
        return obj.start_ts.isoformat()
        
    def get_title(self, obj):
        return "{} to {} - {} - {}<->{}".format(obj.start_ts.time(), (obj.start_ts + datetime.timedelta(minutes = obj.minutes)).time(), obj.customer, obj.customer_language, obj.other_language)
    
    def get_end(self, obj):
        return (obj.start_ts + datetime.timedelta(minutes = obj.minutes)).isoformat()
        
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
        
        
class TranslatorModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslatorMode
        fields = "__all__"
        
class LanguageShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"
        

class TranslatorAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslatorAvailability
        fields = "__all__" 
        ordering = ["dow"]
        
class TelModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = TelModel
		fields = "__all__"
		
class ComputerModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = ComputerModel
		fields = "__all__"
		
class TabletModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = TabletModel
		fields = "__all__"
		
class CableInternetSerializer(serializers.ModelSerializer):
	class Meta:
		model = CableInternet
		fields = "__all__"
		
class CableInternetProviderSerializer(serializers.ModelSerializer):
	class Meta:
		model = CableInternetProvider
		fields = "__all__"
		
class MobileInternetSerializer(serializers.ModelSerializer):
	class Meta:
		model = MobileInternet
		fields = "__all__"
		
class MobileInternetProviderSerializer(serializers.ModelSerializer):
	class Meta:
		model = MobileInternetProvider
		fields = "__all__"
		

        
class TranslatorAvailabilityExceptionSerializer(serializers.ModelSerializer):
    start = serializers.SerializerMethodField()
    end = serializers.SerializerMethodField()
    
    def get_start(self,obj):
        return str(obj.date_from.isoformat())
    def get_end(self,obj):
        return str(obj.date_to.isoformat())
    class Meta:
        model = TranslatorAvailabilityException
        fields = ["start","end"]
        
class CertificationSerializer(serializers.ModelSerializer):
    issuer = CertificationIssuerSerializer()
    #level = CertificationLevelSerializer()
    language_from = LanguageShortSerializer()
    language_to = LanguageShortSerializer()
    class Meta:
        model = Certification
        fields = "__all__"
        
class MicroVocabularyCompactSerializer(serializers.ModelSerializer):
    class Meta:
        model = MicroVocabulary
        fields = "__all__"
        
class TranslatorMicrovocSerializer(serializers.ModelSerializer):
    microvoc = MicroVocabularyCompactSerializer()
    class Meta:
        model = TranslatorMicrovoc
        fields = "__all__"
        
class TranslatorLanguageSerializer(serializers.ModelSerializer):
    language_from = LanguageShortSerializer()
    language_to = LanguageShortSerializer()
    level = LanguageLevelSerializer()
    microvoc = TranslatorMicrovocSerializer(many=True)
    certification = CertificationSerializer()
    class Meta:
        model = TranslatorLanguage
        fields = "__all__"

class TranslatorProfileShortSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    native_lang_1 = LanguageShortSerializer()
    native_lang_2 = LanguageShortSerializer()
    
    def get_full_name(self, obj):
        return u"%s %s" % (obj.user.first_name, obj.user.last_name)
    class Meta:
        model = TranslatorProfile
        fields = "__all__"
        
        
class TranslatorFromLanguageSerializer(serializers.ModelSerializer):
    language_from = LanguageShortSerializer()
    level = LanguageLevelSerializer()
    microvoc = TranslatorMicrovocSerializer(many=True)
    certification = CertificationSerializer()
    class Meta:
        model = TranslatorLanguage
        fields = "__all__"
                
        
class TranslatorInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslatorInvoice
        fields = "__all__"
        
class TranslatorToLanguageSerializer(serializers.ModelSerializer):
    language_to = LanguageShortSerializer()
    level = LanguageLevelSerializer()
    microvoc = TranslatorMicrovocSerializer(many=True)
    certification = CertificationSerializer()
    translator = TranslatorProfileShortSerializer()
    
    class Meta:
        model = TranslatorLanguage
        fields = "__all__"
        
class TranslatorProfileSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    languages = TranslatorLanguageSerializer(many=True)
    native_lang_1 = LanguageShortSerializer()
    native_lang_2 = LanguageShortSerializer()
    invoices = TranslatorInvoiceSerializer(many=True)
    appointments = AppointmentSerializer(many=True)
    availabilities = TranslatorAvailabilitySerializer(many=True)
    exceptions = TranslatorAvailabilityExceptionSerializer(many=True)

    def get_full_name(self, obj):
        return u"%s %s" % (obj.user.first_name, obj.user.last_name)
    class Meta:
        model = TranslatorProfile
        fields = [
            "id", 
            "full_name", "languages","native_lang_1","native_lang_2", "invoices", "availabilities", "appointments", "exceptions",
            "tel_home", "tel_office", "tel_private_cell", "tel_work_cell", "fax", "skype", "secondary_mail", "tel_model",
            "computer_model", "tablet_model", "cable_internet", "cable_internet_provider", "mobile_internet", "mobile_internet_provider",
            "birth_city", "birth_country", "native_lang_1", "native_lang_2", "Nationality", "home_address", "home_city",
            "home_country", "title", #"timezone",
            "vat_num", "soc_num", "bank", "iban", "swift", "paypal", "picture", "video_pres",
            "id_card", "passport", "vat_pic", "notes",
        ]
        
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

class CustomerProfileSerializer(serializers.ModelSerializer):
    users = CustomerUserSerializer(many=True)
    transactions = TransactionSerializer(many=True)
    assignments = CreditAssignmentSerializer(many=True)
    class Meta:
        model = CustomerProfile
        fields = "__all__"
        
class LanguageSerializer(serializers.ModelSerializer):
    #translate_to = TranslatorToLanguageSerializer(many=True)
    #translate_from = TranslatorFromLanguageSerializer(many=True)
    class Meta:
        model = Language
        fields = "__all__"
        

class TranslatorMicrovocFullSerializer(serializers.ModelSerializer):
    translator = TranslatorProfileSerializer()
    lang = TranslatorLanguageSerializer()
    class Meta:
        model = TranslatorMicrovoc
        fields = "__all__"
        
class MicroVocabularySerializer(serializers.ModelSerializer):
    languages = TranslatorMicrovocFullSerializer(many=True)
    class Meta:
        model = MicroVocabulary
        fields = "__all__"
        
        