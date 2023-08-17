# Generated by Django 4.1.3 on 2023-04-10 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USMAApp', '0004_allprojects'),
    ]

    operations = [
        migrations.AddField(
            model_name='allprojects',
            name='Github',
            field=models.CharField(blank=True, default='https://github.com/dimosojunior/', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='allprojects',
            name='StudentEmail',
            field=models.EmailField(blank=True, default='@gmail.com', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='allprojects',
            name='StudentPhoneNumber',
            field=models.CharField(blank=True, default='+255', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='allprojects',
            name='WhatsappLink',
            field=models.CharField(blank=True, default='www.whatsapp.com', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='allprojects',
            name='Youtube',
            field=models.CharField(blank=True, default='www.youtube.com', max_length=1000, null=True),
        ),
    ]
