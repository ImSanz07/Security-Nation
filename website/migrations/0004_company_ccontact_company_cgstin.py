# Generated by Django 4.2 on 2023-04-28 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_company_cemail_company_cpassw_company_uname'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='ccontact',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='cgstin',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
