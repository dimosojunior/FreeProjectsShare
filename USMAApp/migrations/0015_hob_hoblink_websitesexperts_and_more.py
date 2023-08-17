# Generated by Django 4.1.3 on 2023-08-06 09:31

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('USMAApp', '0014_remove_dituniversitycourses_university_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hob',
            name='HobLink',
            field=models.CharField(blank=True, default='USMA/', max_length=500, null=True),
        ),
        migrations.CreateModel(
            name='WebsitesExperts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentName', models.CharField(max_length=500)),
                ('StudentPlace', models.CharField(blank=True, max_length=100, null=True)),
                ('Body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('ShortDescription', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('StudentImage', models.ImageField(blank=True, null=True, upload_to='media/Hob/')),
                ('Github', models.CharField(blank=True, default='www.github.com', max_length=1000, null=True)),
                ('Youtube', models.CharField(blank=True, default='www.youtube.com', max_length=1000, null=True)),
                ('Email', models.CharField(blank=True, default='juniordimoso@gmail.com', max_length=500, null=True)),
                ('Instagram', models.CharField(blank=True, default='www.instagram.com', max_length=1000, null=True)),
                ('Whatsapp', models.CharField(blank=True, default='www.whatsapp.com', max_length=1000, null=True)),
                ('Phone', models.CharField(blank=True, default='+255 628 431 507', max_length=13, null=True)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('CategoryName', models.ForeignKey(max_length=1000, on_delete=django.db.models.deletion.CASCADE, to='USMAApp.hob')),
            ],
            options={
                'verbose_name_plural': 'WebsitesExperts',
            },
        ),
        migrations.CreateModel(
            name='MobileApplicationsExperts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentName', models.CharField(max_length=500)),
                ('StudentPlace', models.CharField(blank=True, max_length=100, null=True)),
                ('Body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('ShortDescription', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('StudentImage', models.ImageField(blank=True, null=True, upload_to='media/Hob/')),
                ('Github', models.CharField(blank=True, default='www.github.com', max_length=1000, null=True)),
                ('Youtube', models.CharField(blank=True, default='www.youtube.com', max_length=1000, null=True)),
                ('Email', models.CharField(blank=True, default='juniordimoso@gmail.com', max_length=500, null=True)),
                ('Instagram', models.CharField(blank=True, default='www.instagram.com', max_length=1000, null=True)),
                ('Whatsapp', models.CharField(blank=True, default='www.whatsapp.com', max_length=1000, null=True)),
                ('Phone', models.CharField(blank=True, default='+255 628 431 507', max_length=13, null=True)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('CategoryName', models.ForeignKey(max_length=1000, on_delete=django.db.models.deletion.CASCADE, to='USMAApp.hob')),
            ],
            options={
                'verbose_name_plural': 'MobileApplicationsExperts',
            },
        ),
        migrations.CreateModel(
            name='MachineLearningExperts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentName', models.CharField(max_length=500)),
                ('StudentPlace', models.CharField(blank=True, max_length=100, null=True)),
                ('Body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('ShortDescription', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('StudentImage', models.ImageField(blank=True, null=True, upload_to='media/Hob/')),
                ('Github', models.CharField(blank=True, default='www.github.com', max_length=1000, null=True)),
                ('Youtube', models.CharField(blank=True, default='www.youtube.com', max_length=1000, null=True)),
                ('Email', models.CharField(blank=True, default='juniordimoso@gmail.com', max_length=500, null=True)),
                ('Instagram', models.CharField(blank=True, default='www.instagram.com', max_length=1000, null=True)),
                ('Whatsapp', models.CharField(blank=True, default='www.whatsapp.com', max_length=1000, null=True)),
                ('Phone', models.CharField(blank=True, default='+255 628 431 507', max_length=13, null=True)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('CategoryName', models.ForeignKey(max_length=1000, on_delete=django.db.models.deletion.CASCADE, to='USMAApp.hob')),
            ],
            options={
                'verbose_name_plural': 'MachineLearningExperts',
            },
        ),
        migrations.CreateModel(
            name='GraphicsDesignerExperts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentName', models.CharField(max_length=500)),
                ('StudentPlace', models.CharField(blank=True, max_length=100, null=True)),
                ('Body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('ShortDescription', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('StudentImage', models.ImageField(blank=True, null=True, upload_to='media/Hob/')),
                ('Github', models.CharField(blank=True, default='www.github.com', max_length=1000, null=True)),
                ('Youtube', models.CharField(blank=True, default='www.youtube.com', max_length=1000, null=True)),
                ('Email', models.CharField(blank=True, default='juniordimoso@gmail.com', max_length=500, null=True)),
                ('Instagram', models.CharField(blank=True, default='www.instagram.com', max_length=1000, null=True)),
                ('Whatsapp', models.CharField(blank=True, default='www.whatsapp.com', max_length=1000, null=True)),
                ('Phone', models.CharField(blank=True, default='+255 628 431 507', max_length=13, null=True)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('CategoryName', models.ForeignKey(max_length=1000, on_delete=django.db.models.deletion.CASCADE, to='USMAApp.hob')),
            ],
            options={
                'verbose_name_plural': 'GraphicsDesignerExperts',
            },
        ),
        migrations.CreateModel(
            name='DataAnalysisandVisualizationExperts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentName', models.CharField(max_length=500)),
                ('StudentPlace', models.CharField(blank=True, max_length=100, null=True)),
                ('Body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('ShortDescription', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('StudentImage', models.ImageField(blank=True, null=True, upload_to='media/Hob/')),
                ('Github', models.CharField(blank=True, default='www.github.com', max_length=1000, null=True)),
                ('Youtube', models.CharField(blank=True, default='www.youtube.com', max_length=1000, null=True)),
                ('Email', models.CharField(blank=True, default='juniordimoso@gmail.com', max_length=500, null=True)),
                ('Instagram', models.CharField(blank=True, default='www.instagram.com', max_length=1000, null=True)),
                ('Whatsapp', models.CharField(blank=True, default='www.whatsapp.com', max_length=1000, null=True)),
                ('Phone', models.CharField(blank=True, default='+255 628 431 507', max_length=13, null=True)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('CategoryName', models.ForeignKey(max_length=1000, on_delete=django.db.models.deletion.CASCADE, to='USMAApp.hob')),
            ],
            options={
                'verbose_name_plural': 'DataAnalysisandVisualizationExperts',
            },
        ),
        migrations.CreateModel(
            name='ComputerVisionExperts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentName', models.CharField(max_length=500)),
                ('StudentPlace', models.CharField(blank=True, max_length=100, null=True)),
                ('Body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('ShortDescription', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('StudentImage', models.ImageField(blank=True, null=True, upload_to='media/Hob/')),
                ('Github', models.CharField(blank=True, default='www.github.com', max_length=1000, null=True)),
                ('Youtube', models.CharField(blank=True, default='www.youtube.com', max_length=1000, null=True)),
                ('Email', models.CharField(blank=True, default='juniordimoso@gmail.com', max_length=500, null=True)),
                ('Instagram', models.CharField(blank=True, default='www.instagram.com', max_length=1000, null=True)),
                ('Whatsapp', models.CharField(blank=True, default='www.whatsapp.com', max_length=1000, null=True)),
                ('Phone', models.CharField(blank=True, default='+255 628 431 507', max_length=13, null=True)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('CategoryName', models.ForeignKey(max_length=1000, on_delete=django.db.models.deletion.CASCADE, to='USMAApp.hob')),
            ],
            options={
                'verbose_name_plural': 'ComputerVisionExperts',
            },
        ),
        migrations.CreateModel(
            name='ComputerMaintenanceExperts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentName', models.CharField(max_length=500)),
                ('StudentPlace', models.CharField(blank=True, max_length=100, null=True)),
                ('Body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('ShortDescription', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('StudentImage', models.ImageField(blank=True, null=True, upload_to='media/Hob/')),
                ('Github', models.CharField(blank=True, default='www.github.com', max_length=1000, null=True)),
                ('Youtube', models.CharField(blank=True, default='www.youtube.com', max_length=1000, null=True)),
                ('Email', models.CharField(blank=True, default='juniordimoso@gmail.com', max_length=500, null=True)),
                ('Instagram', models.CharField(blank=True, default='www.instagram.com', max_length=1000, null=True)),
                ('Whatsapp', models.CharField(blank=True, default='www.whatsapp.com', max_length=1000, null=True)),
                ('Phone', models.CharField(blank=True, default='+255 628 431 507', max_length=13, null=True)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('CategoryName', models.ForeignKey(max_length=1000, on_delete=django.db.models.deletion.CASCADE, to='USMAApp.hob')),
            ],
            options={
                'verbose_name_plural': 'ComputerMaintenanceExperts',
            },
        ),
        migrations.CreateModel(
            name='AutomationExperts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentName', models.CharField(max_length=500)),
                ('StudentPlace', models.CharField(blank=True, max_length=100, null=True)),
                ('Body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('ShortDescription', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('StudentImage', models.ImageField(blank=True, null=True, upload_to='media/Hob/')),
                ('Github', models.CharField(blank=True, default='www.github.com', max_length=1000, null=True)),
                ('Youtube', models.CharField(blank=True, default='www.youtube.com', max_length=1000, null=True)),
                ('Email', models.CharField(blank=True, default='juniordimoso@gmail.com', max_length=500, null=True)),
                ('Instagram', models.CharField(blank=True, default='www.instagram.com', max_length=1000, null=True)),
                ('Whatsapp', models.CharField(blank=True, default='www.whatsapp.com', max_length=1000, null=True)),
                ('Phone', models.CharField(blank=True, default='+255 628 431 507', max_length=13, null=True)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('CategoryName', models.ForeignKey(max_length=1000, on_delete=django.db.models.deletion.CASCADE, to='USMAApp.hob')),
            ],
            options={
                'verbose_name_plural': 'AutomationExperts',
            },
        ),
    ]
