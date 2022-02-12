# Generated by Django 3.2.12 on 2022-02-12 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('centers', '0002_add_postgres_extensions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CenterRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.SmallIntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], db_index=True, default=0, verbose_name='rating')),
                ('comment', models.CharField(blank=True, max_length=1000, verbose_name='comment')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
                ('testing_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='centers.testingcenter')),
            ],
            options={
                'verbose_name': 'center rating',
                'verbose_name_plural': 'center ratings',
            },
        ),
    ]