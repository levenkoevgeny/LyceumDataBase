from django.db import models

CLASS_IN_SCHOOL_CHOICES = {
    7: "7 класс",
    8: "8 класс",
    9: "9 класс",
    10: "10 класс",
}


class AddressRegion(models.Model):
    region = models.CharField(max_length=255, verbose_name="Область")

    def __str__(self):
        return self.region + ' область'

    class Meta:
        verbose_name = 'Адрес (область)'
        verbose_name_plural = 'Адрес (области)'
        ordering = ("region",)


class AddressDistrict(models.Model):
    district = models.CharField(max_length=255, verbose_name="Район")
    region = models.ForeignKey(AddressRegion, on_delete=models.CASCADE)

    def __str__(self):
        return self.district + ' район ' + self.region.region + ' область'

    class Meta:
        verbose_name = 'Адрес (район)'
        verbose_name_plural = 'Адрес (районы)'
        ordering = ("district",)


class AddressCity(models.Model):
    city = models.CharField(max_length=255, verbose_name="Город")
    district = models.ForeignKey(AddressDistrict, on_delete=models.CASCADE)

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'Адрес (город)'
        verbose_name_plural = 'Адрес (город)'
        ordering = ("city",)


class LanguageMath(models.Model):
    language = models.CharField(max_length=100, verbose_name='Язык для математики')

    def __str__(self):
        return self.language

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'
        ordering = ("language",)


class Subject(models.Model):
    subject = models.CharField(max_length=100, verbose_name='Предмет')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
        ordering = ("subject",)


class ForeignLanguage(models.Model):
    foreign_language = models.CharField(max_length=100, verbose_name='Предмет')

    def __str__(self):
        return self.foreign_language

    class Meta:
        verbose_name = 'Иностранный язык для изучения'
        verbose_name_plural = 'Иностранные языки для изучения'
        ordering = ("foreign_language",)


class CompleteFrom(models.Model):
    complete_from = models.CharField(max_length=255)

    def __str__(self):
        return self.complete_from

    class Meta:
        verbose_name = 'Комплектующий орган'
        verbose_name_plural = 'Комплектующие органы'
        ordering = ("complete_from",)


class Privilege(models.Model):
    privilege = models.CharField(max_length=255)

    def __str__(self):
        return self.privilege

    class Meta:
        verbose_name = 'Льгота'
        verbose_name_plural = 'Льготы'
        ordering = ("privilege",)


class VVK(models.Model):
    vvk_result = models.CharField(max_length=255)

    def __str__(self):
        return self.vvk_result

    class Meta:
        verbose_name = 'ВВК результат'
        verbose_name_plural = 'ВВК результаты'
        ordering = ("vvk_result",)


class ApplicantPersonalFile(models.Model):
    last_name = models.CharField(verbose_name="Фамилия", max_length=200)
    first_name = models.CharField(verbose_name="Имя", max_length=200)
    patronymic = models.CharField(verbose_name="Отчество", max_length=200, blank=True, null=True)
    date_of_birth = models.DateField(verbose_name="Дата рождения")
    address_city = models.ForeignKey(AddressCity, verbose_name="Адрес (город)", on_delete=models.SET_NULL, blank=True,
                                     null=True)
    address = models.TextField(verbose_name="Домашний адрес (Улица, Номер дома, Номер квартиры)", blank=True, null=True)
    contact_number = models.TextField(verbose_name="Контактные данные законных представителей")
    complete_from = models.ForeignKey(CompleteFrom, verbose_name="Комплектующий орган", on_delete=models.CASCADE)
    average_mark = models.FloatField(verbose_name="Средний бал свидетельства об общем базовом образовании", blank=True,
                                     null=True)
    average_mark_year = models.FloatField(verbose_name="Средний бал ведомости годовых отметок", blank=True, null=True)
    class_he_goes_to = models.IntegerField(verbose_name="В какой класс поступает", choices=CLASS_IN_SCHOOL_CHOICES)
    there_is_application = models.BooleanField(verbose_name="Заявление (да/нет)", default=False)
    there_is_birth_certificate = models.BooleanField(verbose_name="Свидетельство о рождении (да/нет)", default=False)
    there_is_mark_sheet = models.BooleanField(verbose_name="Ведомость годовых отметок (да/нет)", default=False)
    there_is_characteristic = models.BooleanField(verbose_name="Характеристика (да/нет)", default=False)
    there_is_certificate_of_education = models.BooleanField(
        verbose_name="Свидетельство об общем базовом образовании (да/нет)",
        default=False)
    privilege = models.ForeignKey(Privilege, verbose_name="Документы, подтверждающие право на льготы",
                                  on_delete=models.SET_NULL, blank=True, null=True)
    there_is_conclusion = models.BooleanField(verbose_name="Заключение об изучении кандидата (да/нет)")
    there_is_medical_certificate = models.BooleanField(verbose_name="Медицинская справка (да/нет)", default=False)
    there_is_card_extract = models.BooleanField(
        verbose_name="Выписка из медицинской карты за последние 5 лет  (да/нет)", default=False)
    there_is_psychological_information = models.BooleanField(
        verbose_name="Медицинская справка о состоянии здоровья, подтверждающая отсутствие учета", default=False)
    language_math = models.ForeignKey(LanguageMath, verbose_name="Язык задания по математике",
                                      on_delete=models.SET_NULL, related_name="language_math", blank=True, null=True)
    language_for_dictation = models.ForeignKey(Subject, verbose_name="Выбор учебного предмета для написания диктанта",
                                               on_delete=models.SET_NULL,
                                               blank=True, null=True)
    rus_mark = models.IntegerField(verbose_name="Отметка по Русский язык", blank=True, null=True)
    bel_mark = models.IntegerField(verbose_name="Отметка по Белорусский язык", blank=True, null=True)
    math_mark = models.IntegerField(verbose_name="Отметка по Математика", blank=True, null=True)
    sum_mark = models.IntegerField(verbose_name="Сумма баллов по результатам вступительных испытаний", blank=True,
                                   null=True)
    average_mark_exams = models.FloatField(verbose_name="Средний балл по результатам сдачи экзаменов", blank=True,
                                           null=True)
    language_for_study = models.ForeignKey(ForeignLanguage, verbose_name="Иностранный язык в случае поступления",
                                           on_delete=models.SET_NULL,
                                           blank=True, null=True)
    fit = models.ForeignKey(VVK, verbose_name="Прохождение ВВК",
                            on_delete=models.SET_NULL,
                            blank=True, null=True)
    fit_diagnosis = models.TextField(verbose_name="Диагноз (если не годен)", blank=True, null=True)
    extra_data = models.TextField(verbose_name="Примечание", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания записи")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время последнего редактирования записи")

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'Личное дело'
        verbose_name_plural = 'Личные дела'
        ordering = ("-created_at",)
