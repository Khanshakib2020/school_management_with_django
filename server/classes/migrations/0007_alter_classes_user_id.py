# Generated by Django 4.2.4 on 2023-09-01 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_users_rollnumber'),
        ('classes', '0006_alter_classes_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='user_id',
            field=models.ManyToManyField(blank=True, to='users.users'),
        ),
    ]
