# Generated by Django 5.0.3 on 2024-04-09 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicantpersonalfile',
            name='address_district',
        ),
        migrations.RemoveField(
            model_name='applicantpersonalfile',
            name='address_region',
        ),
    ]