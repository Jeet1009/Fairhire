# Generated by Django 4.0.6 on 2023-02-28 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fairhireapp', '0004_user_logged'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='userid',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
