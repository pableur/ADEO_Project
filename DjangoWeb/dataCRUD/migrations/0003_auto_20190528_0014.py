# Generated by Django 2.2 on 2019-05-27 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataCRUD', '0002_prg_student_site_idcsv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_internship',
            name='REMUNERATION',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
