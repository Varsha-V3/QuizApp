# Generated by Django 2.2.13 on 2020-10-04 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0014_auto_20201004_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.CharField(choices=[('Python', 'Python'), ('Linux', 'Linux')], default='Python', max_length=5, verbose_name='Category'),
        ),
    ]
