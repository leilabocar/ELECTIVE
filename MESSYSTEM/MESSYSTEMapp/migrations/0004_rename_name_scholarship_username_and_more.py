# Generated by Django 4.0.2 on 2022-05-26 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MESSYSTEMapp', '0003_rename_lrn_student_scholarship_lrn_scholarship'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scholarship',
            old_name='name',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='studentinfo',
            old_name='name',
            new_name='username',
        ),
    ]
