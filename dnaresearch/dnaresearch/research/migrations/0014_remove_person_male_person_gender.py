# Generated by Django 4.0.3 on 2022-04-20 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0013_criminalarticles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='male',
        ),
        migrations.AddField(
            model_name='person',
            name='gender',
            field=models.CharField(choices=[('Мужской', 'Мужской'), ('Мужской', 'Женский')], default='Мужской', max_length=7),
        ),
    ]
