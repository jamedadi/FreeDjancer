# Generated by Django 3.2 on 2022-08-25 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20220823_0611'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='portfolio',
            table='portfolio',
        ),
        migrations.AlterModelTable(
            name='portfoliofile',
            table='portfolio_file',
        ),
        migrations.AlterModelTable(
            name='relation',
            table='relation',
        ),
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
        migrations.AlterModelTable(
            name='userskill',
            table='user_skill',
        ),
    ]