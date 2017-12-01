from rest_framework import routers

from .viewsets import *
router = routers.SimpleRouter()

router.register(r'languages',LanguageViewSet)
router.register(r'languagelevels',LanguageLevelViewSet)
router.register(r'certificationlevels',CertificationLevelViewSet)
router.register(r'persontitles',PersonTitleViewSet)
router.register(r'certificationissuers',CertificationIssuerViewSet)
router.register(r'microvocabularies',MicroVocabularyViewSet)
router.register(r'certifications',CertificationViewSet)
router.register(r'translatorprofiles',TranslatorProfileViewSet)
router.register(r'translatorlanguages',TranslatorLanguageViewSet)
router.register(r'translatormicrovocs',TranslatorMicrovocViewSet)
router.register(r'translatormodes',TranslatorModeViewSet)
router.register(r'customerprofiles',CustomerProfileViewSet)
router.register(r'customerusers',CustomerUserViewSet)
router.register(r'creditassignments',CreditAssignmentViewSet)
router.register(r'transactions',TransactionViewSet)
router.register(r'appointments',AppointmentViewSet)
router.register(r'appointmentclosures',AppointmentClosureViewSet)
router.register(r'appointmentevaluations',AppointmentEvaluationViewSet)
router.register(r'translatorinvoices',TranslatorInvoiceViewSet)
router.register(r'translatoravailabilities',TranslatorAvailabilityViewSet)
router.register(r'translatoravailabilityexceptions',TranslatorAvailabilityExceptionViewSet)

router.register(r"telmodel", TelModelViewset)
router.register(r"computermodel", ComputerModelViewset)
router.register(r"tabletmodel", TabletModelViewset)
router.register(r"cableinternet", CableInternetViewset)
router.register(r"cableinternetprovider", CableInternetProviderViewset)
router.register(r"mobileinternet", MobileInternetViewset)
router.register(r"mobileinternetprovider", MobileInternetProviderViewset)


urls = router.urls
