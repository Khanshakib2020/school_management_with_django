# Generated by Django 4.2.4 on 2023-09-01 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_users_rollnumber_alter_users_username'),
        ('subjects', '0003_subjects_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects',
            name='user_id',
            field=models.ManyToManyField(to='users.users'),
        ),
    ]
