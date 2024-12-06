# Generated by Django 5.1.2 on 2024-12-03 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employermodule', '0002_alter_jobdetails_job_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobdetails',
            name='job_type',
            field=models.CharField(choices=[('fulltime', 'Full-time'), ('parttime', 'Part-time'), ('contract', 'Contract')], max_length=20),
        ),
    ]