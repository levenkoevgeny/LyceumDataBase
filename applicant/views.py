import random

from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import ApplicantPersonalFile, CompleteFrom, LanguageMath, ForeignLanguage, Privilege, Subject, VVK
from .filters import ApplicantFilter
from .forms import ApplicantForm
from faker import Faker


@login_required
def applicant_list(request):
    f = ApplicantFilter(request.GET, queryset=ApplicantPersonalFile.objects.all())
    paginator = Paginator(f.qs, 30)
    page = request.GET.get('page')
    applicant_list = paginator.get_page(page)
    applicant_form = ApplicantForm()
    return render(request, 'applicant/applicant_list.html',
                  {'applicant_list': applicant_list, 'applicant_form': applicant_form, 'filter': f})


@login_required
def init_db(request):
    if request.method == 'POST':
        pass
    else:
        CompleteFrom.objects.all().delete()
        CompleteFrom.objects.create(pk=1, complete_from="Комплектующий орган 1")
        CompleteFrom.objects.create(pk=2, complete_from="Комплектующий орган 2")

        LanguageMath.objects.all().delete()
        LanguageMath.objects.create(pk=1, language="русский")
        LanguageMath.objects.create(pk=2, language="белоруский")

        ForeignLanguage.objects.all().delete()
        ForeignLanguage.objects.create(pk=1, foreign_language="анлийский")
        ForeignLanguage.objects.create(pk=2, foreign_language="немецкий")

        Privilege.objects.all().delete()
        Privilege.objects.create(pk=1, privilege='сирота')
        Privilege.objects.create(pk=2, privilege='опека')
        Subject.objects.all().delete()
        Subject.objects.create(pk=1, subject='русский язык')
        Subject.objects.create(pk=2, subject='белорусский язык')
        VVK.objects.all().delete()
        VVK.objects.create(pk=1, vvk_result="годен")
        VVK.objects.create(pk=2, vvk_result="не годен")

        ApplicantPersonalFile.objects.all().delete()

        fake = Faker('ru_RU')
        for i in range(10000):
            random_complete_from = CompleteFrom.objects.get(pk=random.randint(1, 2))
            random_privilege = Privilege.objects.get(pk=random.randint(1, 2))
            random_language_math = LanguageMath.objects.get(pk=random.randint(1, 2))
            random_subject = Subject.objects.get(pk=random.randint(1, 2))
            random_foreign_language = ForeignLanguage.objects.get(pk=random.randint(1, 2))
            random_vvk = VVK.objects.get(pk=random.randint(1, 2))
            ApplicantPersonalFile.objects.create(
                registration_number=fake.passport_number(),
                last_name=fake.last_name(),
                first_name=fake.first_name(),
                date_of_birth=fake.date_of_birth(minimum_age=14, maximum_age=16),
                address=fake.address(),
                contact_number=fake.phone_number(),
                complete_from=random_complete_from,
                average_mark=fake.pyfloat(right_digits=1, positive=True, min_value=6, max_value=9),
                class_he_goes_to=fake.pyint(min_value=7, max_value=10),
                there_is_application=fake.pybool(),
                there_is_birth_certificate=fake.pybool(),
                there_is_mark_sheet=fake.pybool(),
                there_is_characteristic=fake.pybool(),
                there_is_certificate_of_education=fake.pybool(),
                privilege=random_privilege,
                there_is_conclusion=fake.pybool(),
                there_is_medical_certificate=fake.pybool(),
                there_is_card_extract=fake.pybool(),
                there_is_psychological_information=fake.pybool(),
                language_math=random_language_math,
                language_for_dictation=random_subject,
                rus_mark=fake.pyint(min_value=7, max_value=10),
                bel_mark=fake.pyint(min_value=7, max_value=10),
                math_mark=fake.pyint(min_value=7, max_value=10),
                sum_mark=fake.pyint(min_value=7, max_value=10),
                language_for_study=random_foreign_language,
                fit=random_vvk
            )

        return HttpResponse("DB init is completed!!!")
