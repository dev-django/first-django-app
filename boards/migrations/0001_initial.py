# Generated by Django 4.2.4 on 2023-08-27 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='제목')),
                ('text', models.CharField(max_length=512, verbose_name='내용')),
                ('like_count', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(verbose_name='게시일')),
            ],
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=256, verbose_name='내용')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.post')),
            ],
        ),
    ]