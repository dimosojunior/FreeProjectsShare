# Generated by Django 4.1.3 on 2023-08-08 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USMAApp', '0019_remove_experts_shortdescription_alter_experts_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlescategory',
            name='ShortDescription',
        ),
        migrations.AddField(
            model_name='articlescategory',
            name='Title',
            field=models.CharField(default='How to start learning ---------', max_length=1000),
        ),
    ]
