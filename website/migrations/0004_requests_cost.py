# Generated by Django 4.2 on 2023-04-30 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_requests_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='requests',
            name='cost',
            field=models.IntegerField(null=True),
        ),
    ]