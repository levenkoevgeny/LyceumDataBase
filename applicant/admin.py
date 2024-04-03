from django.contrib import admin
from applicant.models import LanguageMath, ForeignLanguage, Subject, Privilege, CompleteFrom, ApplicantPersonalFile, VVK


admin.site.register(LanguageMath)
admin.site.register(ForeignLanguage)
admin.site.register(Subject)
admin.site.register(Privilege)
admin.site.register(CompleteFrom)
admin.site.register(ApplicantPersonalFile)
admin.site.register(VVK)
