# Generated by Django 2.0.5 on 2018-05-10 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180508_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='conekta',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
