# Generated by Django 2.1.8 on 2019-05-22 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('huayuan', '0008_delete_userregister'),
    ]

    operations = [
        migrations.CreateModel(
            name='userRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('useremail', models.EmailField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
