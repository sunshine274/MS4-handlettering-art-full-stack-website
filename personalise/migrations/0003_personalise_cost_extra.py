# Generated by Django 3.1.4 on 2020-12-15 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalise', '0002_auto_20201215_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalise',
            name='cost_extra',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
