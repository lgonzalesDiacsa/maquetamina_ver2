# Generated by Django 4.2 on 2023-04-16 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0010_alter_historial_ubicacion_alter_livedata_ubicacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livedata',
            name='cardidHex',
            field=models.CharField(default='XXXXXXXX', max_length=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='personalregistrado',
            name='cardidHex',
            field=models.CharField(default='XXXXXXXX', max_length=8),
            preserve_default=False,
        ),
    ]
