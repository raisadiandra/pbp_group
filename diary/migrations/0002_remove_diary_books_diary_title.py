# Generated by Django 4.2.6 on 2023-10-28 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diary',
            name='books',
        ),
        migrations.AddField(
            model_name='diary',
            name='title',
            field=models.CharField(default='Untitled', max_length=100),
        ),
    ]
