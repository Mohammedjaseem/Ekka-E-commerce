# Generated by Django 4.1.1 on 2022-10-16 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_deals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deals',
            name='end_date',
            field=models.DateTimeField(),
        ),
    ]
