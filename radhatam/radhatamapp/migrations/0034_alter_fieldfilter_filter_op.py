# Generated by Django 4.1.6 on 2023-02-18 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radhatamapp', '0033_alter_fieldfilter_filter_op'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldfilter',
            name='filter_op',
            field=models.CharField(choices=[('=', 'Exact'), ('!=', 'Not')], default='=', max_length=30),
        ),
    ]
