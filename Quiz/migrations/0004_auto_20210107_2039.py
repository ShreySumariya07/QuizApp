# Generated by Django 3.0.8 on 2021-01-07 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Quiz', '0003_quiz_details_questions_entered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check_answers',
            name='st_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='result',
            name='status',
            field=models.CharField(default=False, max_length=100),
        ),
    ]
