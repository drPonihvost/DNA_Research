# Generated by Django 4.0.4 on 2022-06-28 08:27

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='can_sign',
            field=models.BooleanField(default=False, null=True, verbose_name='Право на подпись'),
        ),
        migrations.AddField(
            model_name='profile',
            name='post_index',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Мобильный телефон'),
        ),
    ]
