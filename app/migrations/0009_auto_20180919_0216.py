# Generated by Django 2.1.1 on 2018-09-19 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20180919_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='representative',
            name='picture',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=''),
        ),
    ]
