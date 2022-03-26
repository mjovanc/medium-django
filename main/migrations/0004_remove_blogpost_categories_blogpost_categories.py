# Generated by Django 4.0.3 on 2022-03-26 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_blogpost_categories_blogpost_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='categories',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='categories',
            field=models.ManyToManyField(to='main.blogcategory'),
        ),
    ]
