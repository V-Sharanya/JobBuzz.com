# Generated by Django 5.1.2 on 2024-12-06 07:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employermodule', '0004_alter_jobdetails_job_type'),
        ('jobseekermodule', '0002_alter_applicant_cgpa_alter_applicant_expected_salary_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('resume', models.FileField(upload_to='resumes/')),
                ('cover_letter', models.TextField()),
                ('job_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employermodule.jobdetails')),
            ],
        ),
    ]
