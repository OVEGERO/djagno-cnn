# Generated by Django 4.2.1 on 2023-05-21 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_pacient_diagnostico'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='diagnostico',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]