# Generated by Django 3.2 on 2022-08-25 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='months',
            field=models.PositiveBigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
