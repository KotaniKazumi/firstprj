# Generated by Django 3.2.6 on 2021-09-13 07:47

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
                ('tile', models.CharField(max_length=200, verbose_name='タイトル')),
                ('content', models.TextField(verbose_name='本文')),
                ('posted_at', models.DateTimeField(auto_now_add=True, verbose_name='投稿日時')),
                ('categry', models.CharField(choices=[('science', '科学のこと'), ('dailylife', '日常のこと'), ('music', '音楽のこと')], max_length=50, verbose_name='カテゴリ')),
            ],
        ),
    ]
