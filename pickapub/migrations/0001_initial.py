# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pubs',
            fields=[
                ('entity_id', models.AutoField(serialize=False, primary_key=True)),
                ('pubname', models.CharField(max_length=45)),
                ('region', models.IntegerField()),
            ],
            options={
                'db_table': 'pubs',
                'managed': False,
            },
        ),
    ]
