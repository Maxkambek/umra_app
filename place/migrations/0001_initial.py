# Generated by Django 4.1.5 on 2023-01-09 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=331)),
                ('image', models.ImageField(upload_to='places/')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Islom tarixiga oid joylar',
                'verbose_name_plural': 'Islom tarixiga oid joylar',
            },
        ),
    ]
