# Generated by Django 4.0.3 on 2022-03-22 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('text', models.TextField(blank=True, max_length=1000, verbose_name='Description')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created Date')),
                ('updated', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Updated Date')),
            ],
            options={
                'verbose_name': 'Blog Post',
                'verbose_name_plural': 'Blog Posts',
            },
        ),
    ]
