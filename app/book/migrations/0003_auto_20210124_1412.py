# Generated by Django 3.1.5 on 2021-01-24 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20210124_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='books',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='book.author'),
            preserve_default=False,
        ),
    ]