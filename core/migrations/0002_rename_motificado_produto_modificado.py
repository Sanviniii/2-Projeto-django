# Generated by Django 3.2.5 on 2023-11-14 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='motificado',
            new_name='modificado',
        ),
    ]
