# Generated by Django 4.0.2 on 2022-05-27 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MESSYSTEMapp', '0004_rename_name_scholarship_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='adviser',
            field=models.CharField(choices=[(' ', ' '), ('Pambid', 'Ms. Gina Pambid'), ('Pendo', 'Mrs. Aurea Pendo'), ('Loresca', 'Ms. Adelia Loresca'), ('Bocar', 'Mrs. Maria Lina Bocar'), ('Camcho', 'Ms. Ella Mae Camcho'), ('Neypes', 'Mr. Khristine Neypes'), ('Niemes', 'Renee Rose Niemes'), ('Apostol', 'Mrs. Teresita Apostol')], max_length=50, verbose_name='adviser'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='gradelvl',
            field=models.CharField(choices=[(' ', ' '), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=11, verbose_name='gradelvl'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='section',
            field=models.CharField(choices=[(' ', ' '), ('A', 'Section A'), ('B', 'Section B'), ('C', 'Section C'), ('D', 'Section D'), ('E', 'Section E'), ('F', 'Section F'), ('G', 'Section G')], max_length=50, verbose_name='section'),
        ),
    ]
