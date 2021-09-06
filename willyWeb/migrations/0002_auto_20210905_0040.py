# Generated by Django 3.2.6 on 2021-09-04 22:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('willyWeb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='teacher',
        ),
        migrations.AddField(
            model_name='registeration',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='competition',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='competition',
            name='date_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='courses',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='courses',
            name='date_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='courses',
            name='status',
            field=models.CharField(choices=[('Available', 'Available'), ('Not Available', 'Not Available')], default=('Available', 'Available'), max_length=50),
        ),
    ]
