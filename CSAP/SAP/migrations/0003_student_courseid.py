# Generated by Django 3.2.6 on 2022-03-31 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SAP', '0002_auto_20220331_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='courseid',
            field=models.CharField(default='NILL', max_length=10),
        ),
    ]
