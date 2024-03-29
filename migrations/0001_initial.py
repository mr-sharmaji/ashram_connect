# Generated by Django 2.2.2 on 2019-06-14 03:51

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('create_date', models.DateTimeField(default=datetime.datetime(2019, 6, 14, 3, 51, 44, 361509, tzinfo=utc))),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete='DO_NOTHING', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('create_date', models.DateTimeField(default=datetime.datetime(2019, 6, 14, 3, 51, 44, 362506, tzinfo=utc))),
                ('comment', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete='DO_NOTHING', related_name='comments', to='blog.Post')),
            ],
        ),
    ]
