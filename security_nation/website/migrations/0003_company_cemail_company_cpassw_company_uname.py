# Generated by Django 4.1.7 on 2023-04-28 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='cemail',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='cpassw',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='uname',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
