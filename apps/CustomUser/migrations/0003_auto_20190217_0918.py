# Generated by Django 2.1.7 on 2019-02-17 09:18

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('CustomUser', '0002_user_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phoneno',
            field=phonenumber_field.modelfields.PhoneNumberField(default=0, max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='category',
            field=models.CharField(choices=[('IN', 'Investor'), ('ME', 'Mentor'), ('FO', 'Founder')], default='IN', max_length=2),
        ),
    ]
