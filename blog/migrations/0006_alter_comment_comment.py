# Generated by Django 4.1 on 2022-09-11 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]