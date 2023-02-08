# Generated by Django 4.1.6 on 2023-02-07 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('A+', 'A(+ve)'), ('A-', 'A(-ve)'), ('B+', 'B(+ve)'), ('B-', 'B(-ve)'), ('O+', 'O(+ve)'), ('O-', 'O(-ve)'), ('AB+', 'AB(+ve)'), ('AB-', 'AB(-ve)')], max_length=255, null=True),
        ),
    ]
