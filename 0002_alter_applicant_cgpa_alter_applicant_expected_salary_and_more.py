# Generated by Django 5.1.2 on 2024-12-03 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobseekermodule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='cgpa',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='expected_salary',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='tenth_marks',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='twelfth_marks',
            field=models.CharField(max_length=5),
        ),
    ]