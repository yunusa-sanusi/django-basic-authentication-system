# Generated by Django 3.2.8 on 2021-10-18 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_student_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(default=18, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='level',
            field=models.CharField(choices=[('100', '100'), ('200', '200'), ('300', '300'), ('400', '400')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='matric_number',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone_number',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone_number',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='staff_id',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='title',
            field=models.CharField(choices=[('Dr', 'Dr'), ('Mr', 'Mr'), ('Miss', 'Miss'), ('Mrs', 'Mrs'), ('Prof', 'Prof')], max_length=5, null=True),
        ),
    ]
