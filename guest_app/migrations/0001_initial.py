# Generated by Django 2.1.1 on 2018-12-16 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('status', models.BooleanField(default=True, verbose_name='状态')),
                ('limit', models.IntegerField(verbose_name='人数')),
                ('address', models.CharField(max_length=100, verbose_name='地址')),
                ('start_time', models.DateTimeField(verbose_name='时间')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('real_name', models.CharField(max_length=64, verbose_name='姓名')),
                ('phone', models.CharField(max_length=16, verbose_name='手机')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('sign', models.BooleanField(verbose_name='签到')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guest_app.Event')),
            ],
        ),
    ]
