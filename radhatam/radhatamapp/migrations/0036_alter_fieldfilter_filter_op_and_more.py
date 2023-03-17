# Generated by Django 4.1.6 on 2023-02-19 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radhatamapp', '0035_alter_fieldfilter_filter_op'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldfilter',
            name='filter_op',
            field=models.CharField(choices=[('EXACT', 'EXACT'), ('NOT', 'NOT')], default='EXACT', max_length=30),
        ),
        migrations.AlterField(
            model_name='fieldfilter',
            name='filter_val',
            field=models.CharField(max_length=120),
        ),
    ]
