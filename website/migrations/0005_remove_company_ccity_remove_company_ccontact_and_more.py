# Generated by Django 4.2 on 2023-04-28 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0004_company_ccontact_company_cgstin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='ccity',
        ),
        migrations.RemoveField(
            model_name='company',
            name='ccontact',
        ),
        migrations.RemoveField(
            model_name='company',
            name='ccost',
        ),
        migrations.RemoveField(
            model_name='company',
            name='cdis',
        ),
        migrations.RemoveField(
            model_name='company',
            name='cemail',
        ),
        migrations.RemoveField(
            model_name='company',
            name='cgstin',
        ),
        migrations.RemoveField(
            model_name='company',
            name='cimage',
        ),
        migrations.RemoveField(
            model_name='company',
            name='cname',
        ),
        migrations.RemoveField(
            model_name='company',
            name='cpassw',
        ),
        migrations.RemoveField(
            model_name='company',
            name='cstate',
        ),
        migrations.RemoveField(
            model_name='company',
            name='czip',
        ),
        migrations.RemoveField(
            model_name='company',
            name='uname',
        ),
        migrations.RemoveField(
            model_name='userm',
            name='passw',
        ),
        migrations.RemoveField(
            model_name='userm',
            name='uname',
        ),
        migrations.AddField(
            model_name='userm',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
