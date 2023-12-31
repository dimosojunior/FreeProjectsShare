# Generated by Django 4.1.3 on 2023-08-08 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('USMAApp', '0017_remove_allprojects_pdffile_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='computermaintenanceexperts',
            name='CategoryName',
        ),
        migrations.RemoveField(
            model_name='computervisionexperts',
            name='CategoryName',
        ),
        migrations.RemoveField(
            model_name='dataanalysisandvisualizationexperts',
            name='CategoryName',
        ),
        migrations.RemoveField(
            model_name='graphicsdesignerexperts',
            name='CategoryName',
        ),
        migrations.RemoveField(
            model_name='machinelearningexperts',
            name='CategoryName',
        ),
        migrations.RemoveField(
            model_name='mobileapplicationsexperts',
            name='CategoryName',
        ),
        migrations.RemoveField(
            model_name='websitesexperts',
            name='CategoryName',
        ),
        migrations.DeleteModel(
            name='AutomationExperts',
        ),
        migrations.DeleteModel(
            name='ComputerMaintenanceExperts',
        ),
        migrations.DeleteModel(
            name='ComputerVisionExperts',
        ),
        migrations.DeleteModel(
            name='DataAnalysisandVisualizationExperts',
        ),
        migrations.DeleteModel(
            name='GraphicsDesignerExperts',
        ),
        migrations.DeleteModel(
            name='MachineLearningExperts',
        ),
        migrations.DeleteModel(
            name='MobileApplicationsExperts',
        ),
        migrations.DeleteModel(
            name='WebsitesExperts',
        ),
    ]
