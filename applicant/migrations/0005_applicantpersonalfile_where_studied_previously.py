# Generated by Django 5.0.3 on 2024-05-31 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0004_applicantpersonalfile_is_chaes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicantpersonalfile',
            name='where_studied_previously',
            field=models.TextField(blank=True, null=True, verbose_name='Учебное заведение, где обучался ранее'),
        ),
    ]
