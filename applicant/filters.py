import django_filters
from django import forms

from .models import LanguageMath, ForeignLanguage, Subject, Privilege, CompleteFrom, ApplicantPersonalFile, VVK, \
    AddressRegion, AddressDistrict, AddressCity

myDateInput = forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'})


class ApplicantFilter(django_filters.FilterSet):
    last_name = django_filters.CharFilter(field_name='last_name', lookup_expr='icontains')
    date_of_birth_gte = django_filters.DateFilter(field_name='date_of_birth', lookup_expr='gte', widget=myDateInput)
    date_of_birth_lte = django_filters.DateFilter(field_name='date_of_birth', lookup_expr='lte', widget=myDateInput)
    complete_from = django_filters.ModelMultipleChoiceFilter(field_name='complete_from',
                                                             queryset=CompleteFrom.objects.all())
    address_region = django_filters.ModelMultipleChoiceFilter(field_name='address_city__district__region',
                                                              queryset=AddressRegion.objects.all())
    address_district = django_filters.ModelMultipleChoiceFilter(field_name='address_city__district',
                                                                queryset=AddressDistrict.objects.all())
    address_city = django_filters.ModelMultipleChoiceFilter(field_name='address_city',
                                                            queryset=AddressCity.objects.all())
    average_mark_gte = django_filters.NumberFilter(field_name='average_mark', lookup_expr='gte')
    average_mark_lte = django_filters.NumberFilter(field_name='average_mark', lookup_expr='lte')

    class_he_goes_to_gte = django_filters.NumberFilter(field_name='class_he_goes_to', lookup_expr='gte')
    class_he_goes_to_lte = django_filters.NumberFilter(field_name='class_he_goes_to', lookup_expr='lte')
    there_is_application = django_filters.BooleanFilter(field_name='there_is_application')
    there_is_birth_certificate = django_filters.BooleanFilter(field_name='there_is_birth_certificate')
    there_is_mark_sheet = django_filters.BooleanFilter(field_name='there_is_mark_sheet')
    there_is_characteristic = django_filters.BooleanFilter(field_name='there_is_characteristic')
    there_is_certificate_of_education = django_filters.BooleanFilter(field_name='there_is_certificate_of_education')
    privilege = django_filters.ModelMultipleChoiceFilter(field_name='privilege', queryset=Privilege.objects.all())


    is_chaes = django_filters.BooleanFilter(field_name='is_chaes')
    is_employee_child = django_filters.BooleanFilter(field_name='is_employee_child')
    is_large_family = django_filters.BooleanFilter(field_name='is_large_family')
    math_mark_after_6_gte = django_filters.NumberFilter(field_name='math_mark_after_6', lookup_expr='gte')
    math_mark_after_6_lte = django_filters.NumberFilter(field_name='math_mark_after_6', lookup_expr='lte')
    physical_training_mark_after_6_gte = django_filters.NumberFilter(field_name='physical_training_mark_after_6', lookup_expr='gte')
    physical_training_mark_after_6_lte = django_filters.NumberFilter(field_name='physical_training_mark_after_6', lookup_expr='lte')


    there_is_conclusion = django_filters.BooleanFilter(field_name='there_is_conclusion')
    there_is_medical_certificate = django_filters.BooleanFilter(field_name='there_is_medical_certificate')
    there_is_card_extract = django_filters.BooleanFilter(field_name='there_is_card_extract')
    there_is_psychological_information = django_filters.BooleanFilter(field_name='there_is_psychological_information')
    language_math = django_filters.ModelMultipleChoiceFilter(field_name='language_math',
                                                             queryset=LanguageMath.objects.all())
    language_for_dictation = django_filters.ModelMultipleChoiceFilter(field_name='language_for_dictation',
                                                                      queryset=Subject.objects.all())
    language_for_study = django_filters.ModelMultipleChoiceFilter(field_name='language_for_study',
                                                                  queryset=ForeignLanguage.objects.all())
    fit = django_filters.ModelMultipleChoiceFilter(field_name='fit',
                                                   queryset=VVK.objects.all())
    rus_mark_gte = django_filters.NumberFilter(field_name='rus_mark', lookup_expr='gte')
    rus_mark_lte = django_filters.NumberFilter(field_name='rus_mark', lookup_expr='lte')
    bel_mark_gte = django_filters.NumberFilter(field_name='bel_mark', lookup_expr='gte')
    bel_mark_lte = django_filters.NumberFilter(field_name='bel_mark', lookup_expr='lte')
    math_mark_gte = django_filters.NumberFilter(field_name='math_mark', lookup_expr='gte')
    math_mark_lte = django_filters.NumberFilter(field_name='math_mark', lookup_expr='lte')

    class Meta:
        model = ApplicantPersonalFile
        fields = []