# Generated by Django 2.2.2 on 2019-06-22 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_guest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='untitled', max_length=50)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField(max_length=500)),
            ],
        ),
    ]