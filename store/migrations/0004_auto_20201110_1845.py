# Generated by Django 3.1.2 on 2020-11-11 00:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20201110_1843'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicios',
            old_name='servicio',
            new_name='servidescrip',
        ),
    ]