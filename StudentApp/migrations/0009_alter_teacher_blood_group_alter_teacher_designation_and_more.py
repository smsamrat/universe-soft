# Generated by Django 4.1.6 on 2023-02-14 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentApp', '0008_alter_teacher_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('A+', 'A(+ve)'), ('A-', 'A(-ve)'), ('B+', 'B(+ve)'), ('B-', 'B(-ve)'), ('O+', 'O(+ve)'), ('O-', 'O(-ve)'), ('AB+', 'AB(+ve)'), ('AB-', 'AB(-ve)')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='designation',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='education',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('C', 'Custom')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='occupation',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
