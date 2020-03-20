# Generated by Django 3.0.4 on 2020-03-15 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=200)),
                ('write', models.TextField()),
            ],
        ),
    ]
