# Generated by Django 5.0.7 on 2024-08-02 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0002_chaivariety_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaivariety',
            name='price',
            field=models.TextField(default=''),
        ),
    ]
