# Generated by Django 4.2.10 on 2024-02-24 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0003_alter_customuser_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('departure', models.DateField()),
                ('arrival', models.DateField()),
                ('budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
