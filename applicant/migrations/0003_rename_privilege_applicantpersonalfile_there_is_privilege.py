# Generated by Django 5.0.3 on 2024-04-03 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0002_alter_applicantpersonalfile_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicantpersonalfile',
            old_name='privilege',
            new_name='there_is_privilege',
        ),
    ]
