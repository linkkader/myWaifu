# Generated by Django 3.1.5 on 2021-01-05 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0005_auto_20210105_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waifu',
            name='bloodType',
            field=models.CharField(default=None, max_length=200000),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='dateBirth',
            field=models.CharField(default=None, max_length=200000),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='description',
            field=models.CharField(default=None, max_length=200000),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='gender',
            field=models.CharField(default=None, max_length=200000),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='img',
            field=models.CharField(default=None, max_length=200000),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='name',
            field=models.CharField(default=None, max_length=200000),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='orName',
            field=models.CharField(default=None, max_length=200000),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='placeOf',
            field=models.CharField(default=None, max_length=200000),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='roName',
            field=models.CharField(default=None, max_length=200000),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='serie',
            field=models.CharField(default=None, max_length=200000),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='type',
            field=models.CharField(default=None, max_length=200000),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='url',
            field=models.CharField(default=None, max_length=200000),
        ),
    ]
