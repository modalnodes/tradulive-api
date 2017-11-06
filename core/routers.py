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

urls = router.urls
