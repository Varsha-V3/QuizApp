# Generated by Django 2.2.10 on 2020-02-11 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_auto_20200210_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.CharField(choices=[('C++', 'C++'), ('Java', 'Java')], default='C++', max_length=5, verbose_name='Category'),
        ),
    ]
