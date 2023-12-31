# Generated by Django 4.0.6 on 2023-02-10 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('type_of_disability', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(null=True)),
                ('company', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('pincode', models.CharField(max_length=100, null=True)),
                ('date', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
