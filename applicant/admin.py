from django.contrib import admin
from applicant.models import LanguageMath, ForeignLanguage, Subject, Privilege, CompleteFrom, ApplicantPersonalFile, \
    VVK, AddressRegion, AddressDistrict, AddressCity

admin.site.register(LanguageMath)
admin.site.register(ForeignLanguage)
admin.site.register(Subject)
admin.site.register(Privilege)
admin.site.register(CompleteFrom)
admin.site.register(ApplicantPersonalFile)
admin.site.register(VVK)
admin.site.register(AddressRegion)
admin.site.register(AddressDistrict)
admin.site.register(AddressCity)
