# Generated by Django 3.2.5 on 2022-03-17 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0003_adminbase_commission'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminbase',
            name='mode_demo',
            field=models.BooleanField(default=False),
        ),
    ]
