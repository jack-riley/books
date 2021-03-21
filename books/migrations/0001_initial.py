# Generated by Django 3.1.6 on 2021-03-21 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=55)),
                ('first_name', models.CharField(max_length=55)),
                ('last_name', models.CharField(max_length=55)),
                ('dob', models.DateField()),
                ('password', models.CharField(max_length=255)),
                ('user_id', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tile', models.CharField(max_length=255)),
                ('author_first_name', models.CharField(blank=True, max_length=55)),
                ('author_last_name', models.CharField(max_length=55)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_likes', models.ManyToManyField(related_name='liked_books', to='books.User')),
                ('user_uploaded', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books_uploaded', to='books.user')),
            ],
        ),
    ]