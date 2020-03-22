# Generated by Django 2.1.3 on 2018-12-14 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_auto_20181214_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendances',
            name='is_excused',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='attendances',
            name='justification',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='attendances',
            name='type',
            field=models.IntegerField(choices=[(0, 'Absent'), (1, 'Present')], default=0),
            preserve_default=False,
        ),
    ]
