# Generated by Django 4.0.3 on 2022-03-20 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0005_alter_person_research'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='research',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='research.research'),
        ),
    ]
