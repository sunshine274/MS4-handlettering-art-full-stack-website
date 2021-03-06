# Generated by Django 3.1.4 on 2020-12-17 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_remove_order_delivery_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='county',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='postcode',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='street_address1',
            field=models.CharField(default='', max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='street_address2',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='town_or_city',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
    ]
