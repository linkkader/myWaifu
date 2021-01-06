# Generated by Django 3.1.5 on 2021-01-05 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_waifu_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='waifu',
            name='blood',
            field=models.CharField(default=None, max_length=60),
        ),
        migrations.AddField(
            model_name='waifu',
            name='dateBirth',
            field=models.CharField(default=None, max_length=60),
        ),
        migrations.AddField(
            model_name='waifu',
            name='description',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='waifu',
            name='gender',
            field=models.CharField(default=None, max_length=60),
        ),
        migrations.AddField(
            model_name='waifu',
            name='height',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='waifu',
            name='hip',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='waifu',
            name='iid',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='waifu',
            name='img',
            field=models.CharField(default=None, max_length=60),
        ),
        migrations.AddField(
            model_name='waifu',
            name='isWaifu',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='waifu',
            name='like',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='waifu',
            name='likeCount',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='waifu',
            name='orName',
            field=models.CharField(default=None, max_length=60),
        ),
        migrations.AddField(
            model_name='waifu',
            name='placeOf',
            field=models.CharField(default=None, max_length=60),
        ),
        migrations.AddField(
            model_name='waifu',
            name='popularity',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='waifu',
            name='roName',
            field=models.CharField(default=None, max_length=60),
        ),
        migrations.AddField(
            model_name='waifu',
            name='serie',
            field=models.CharField(default=None, max_length=60),
        ),
        migrations.AddField(
            model_name='waifu',
            name='trash',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='waifu',
            name='type',
            field=models.CharField(default=None, max_length=60),
        ),
        migrations.AddField(
            model_name='waifu',
            name='url',
            field=models.CharField(default=None, max_length=60),
        ),
        migrations.AddField(
            model_name='waifu',
            name='waist',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='waifu',
            name='weight',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='age',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='id',
            field=models.IntegerField(default=None, primary_key=True, serialize=False),
        ),
    ]