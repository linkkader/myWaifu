# Generated by Django 3.1.5 on 2021-01-06 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0007_auto_20210105_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.IntegerField(default=None, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=200000)),
                ('age', models.IntegerField(default=0)),
                ('type', models.CharField(default='', max_length=200000)),
                ('gender', models.CharField(default='', max_length=200000)),
                ('url', models.CharField(default='', max_length=200000)),
                ('img', models.CharField(default='', max_length=200000)),
                ('orName', models.CharField(default='', max_length=200000)),
                ('roName', models.CharField(default='', max_length=200000)),
                ('placeOf', models.CharField(default='', max_length=200000)),
                ('dateBirth', models.CharField(default='', max_length=200000)),
                ('height', models.IntegerField(default=0)),
                ('weight', models.IntegerField(default=0)),
                ('hip', models.IntegerField(default=0)),
                ('bust', models.IntegerField(default=0)),
                ('waist', models.IntegerField(default=0)),
                ('bloodType', models.CharField(default='', max_length=200000)),
                ('iid', models.IntegerField(default=0)),
                ('description', models.CharField(default='', max_length=200000)),
                ('popularity', models.IntegerField(default=0)),
                ('like', models.IntegerField(default=0)),
                ('trash', models.IntegerField(default=0)),
                ('likeCount', models.IntegerField(default=0)),
                ('trashCount', models.IntegerField(default=0)),
                ('isWaifu', models.BooleanField(default=True)),
                ('serie', models.CharField(default='', max_length=200000)),
            ],
        ),
    ]