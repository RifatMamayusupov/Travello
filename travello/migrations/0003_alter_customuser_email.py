# Generated by Django 4.2.10 on 2024-02-24 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0002_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
