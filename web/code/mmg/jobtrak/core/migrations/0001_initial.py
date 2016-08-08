# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-08 00:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contact', '0001_initial'),
        ('links', '0004_auto_20160729_2305'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('when', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='When')),
                ('note', models.TextField(blank=True, default=b'', verbose_name='Note')),
            ],
            options={
                'get_latest_by': 'when',
                'verbose_name': 'History Item',
                'verbose_name_plural': 'History Items',
            },
        ),
        migrations.CreateModel(
            name='JobListing',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('sourceURL', models.URLField(blank=True, null=True)),
                ('date_posted', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('salary_range', models.CharField(default=b'', max_length=32)),
                ('can_be_remote', models.BooleanField(default=False)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contact.CompanyLocation')),
                ('ref_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contact.Contact', verbose_name='Referred By')),
                ('sourceSite', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='links.JobBoard', verbose_name='Source')),
            ],
            options={
                'verbose_name': 'Job Listing',
                'verbose_name_plural': 'Job Listings',
            },
        ),
        migrations.CreateModel(
            name='JobListingPerson',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('note', models.CharField(blank=True, max_length=255, null=True, verbose_name='Note')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.Contact', verbose_name='Contact')),
                ('joblisting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.JobListing', verbose_name='Job Listing')),
            ],
            options={
                'verbose_name': 'Associated Person',
                'verbose_name_plural': 'Associated People',
            },
        ),
        migrations.CreateModel(
            name='JobListingRole',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.CreateModel(
            name='JobStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('order_id', models.IntegerField(verbose_name='Order')),
            ],
            options={
                'ordering': ['order_id'],
                'verbose_name': 'Job Status',
                'verbose_name_plural': 'Job Statuses',
            },
        ),
        migrations.AddField(
            model_name='joblistingperson',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.JobListingRole', verbose_name='Role'),
        ),
        migrations.AddField(
            model_name='joblisting',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.JobStatus'),
        ),
        migrations.AddField(
            model_name='actionhistory',
            name='joblisting',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.JobListing', verbose_name='Job Listing'),
        ),
        migrations.AddField(
            model_name='actionhistory',
            name='who',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contact.Contact', verbose_name='Contact'),
        ),
    ]
