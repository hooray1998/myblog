# Generated by Django 2.2.1 on 2019-05-17 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190421_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='文章图片'),
        ),
    ]
