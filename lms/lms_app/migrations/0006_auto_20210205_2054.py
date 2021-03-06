# Generated by Django 2.2 on 2021-02-05 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0005_auto_20210205_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='retal_price_day',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('sold', 'sold'), ('rented', 'rented'), ('available', 'available')], max_length=50, null=True),
        ),
    ]
