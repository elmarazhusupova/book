# Generated by Django 4.1.7 on 2023-03-12 09:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('firstname_en', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200)),
                ('lastname_en', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='static/img')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('name_en', models.CharField(blank=True, max_length=200, null=True)),
                ('name_ky', models.CharField(blank=True, max_length=200, null=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('desc_en', models.TextField(blank=True, null=True)),
                ('desc_ky', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='', verbose_name='static/img')),
                ('price', models.FloatField()),
                ('new_price', models.FloatField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, default=None, null=True)),
                ('published_day', models.DateField(blank=True, null=True)),
                ('is_in_stock', models.BooleanField(default=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author', to='product.author')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('title_en', models.CharField(blank=True, max_length=200, null=True)),
                ('title_ky', models.CharField(blank=True, max_length=200, null=True)),
                ('category_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('slug', models.SlugField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_en', models.CharField(blank=True, max_length=200, null=True)),
                ('title_ky', models.CharField(blank=True, max_length=200, null=True)),
                ('books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='product.book')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/img')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('books_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='product.category'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='publisher', to='product.publisher'),
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book', to='product.book'),
        ),
    ]
