# Generated by Django 4.1.3 on 2023-08-06 09:50

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('USMAApp', '0015_hob_hoblink_websitesexperts_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='ArticleLink',
            field=models.CharField(blank=True, default='USMA/', max_length=500, null=True),
        ),
        migrations.CreateModel(
            name='WebsiteArticles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WrittenBy', models.CharField(blank=True, default='Dimoso Junior', max_length=100, null=True)),
                ('ArticleBody', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('ShortDescription', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('ArticleImage', models.ImageField(blank=True, null=True, upload_to='media/ArticlesImage/')),
                ('Github', models.CharField(blank=True, default='www.github.com', max_length=1000, null=True)),
                ('Youtube', models.CharField(blank=True, default='www.youtube.com', max_length=1000, null=True)),
                ('year', models.CharField(blank=True, default='2023', max_length=100, null=True)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='media/ArticlesPDF/')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('ArticlesName', models.ForeignKey(max_length=1000, on_delete=django.db.models.deletion.CASCADE, to='USMAApp.articles')),
            ],
            options={
                'verbose_name_plural': 'WebsiteArticles',
            },
        ),
        migrations.CreateModel(
            name='MobileApplicationsArticles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WrittenBy', models.CharField(blank=True, default='Dimoso Junior', max_length=100, null=True)),
                ('ArticleBody', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('ShortDescription', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('ArticleImage', models.ImageField(blank=True, null=True, upload_to='media/ArticlesImage/')),
                ('Github', models.CharField(blank=True, default='www.github.com', max_length=1000, null=True)),
                ('Youtube', models.CharField(blank=True, default='www.youtube.com', max_length=1000, null=True)),
                ('year', models.CharField(blank=True, default='2023', max_length=100, null=True)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='media/ArticlesPDF/')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('ArticlesName', models.ForeignKey(max_length=1000, on_delete=django.db.models.deletion.CASCADE, to='USMAApp.articles')),
            ],
            options={
                'verbose_name_plural': 'MobileApplicationsArticles',
            },
        ),
        migrations.CreateModel(
            name='AIArticles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WrittenBy', models.CharField(blank=True, default='Dimoso Junior', max_length=100, null=True)),
                ('ArticleBody', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('ShortDescription', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('ArticleImage', models.ImageField(blank=True, null=True, upload_to='media/ArticlesImage/')),
                ('Github', models.CharField(blank=True, default='www.github.com', max_length=1000, null=True)),
                ('Youtube', models.CharField(blank=True, default='www.youtube.com', max_length=1000, null=True)),
                ('year', models.CharField(blank=True, default='2023', max_length=100, null=True)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='media/ArticlesPDF/')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('ArticlesName', models.ForeignKey(max_length=1000, on_delete=django.db.models.deletion.CASCADE, to='USMAApp.articles')),
            ],
            options={
                'verbose_name_plural': 'AIArticles',
            },
        ),
    ]
