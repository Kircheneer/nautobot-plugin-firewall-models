# Generated by Django 3.1.13 on 2022-04-20 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("nautobot_firewall_models", "0002_role"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="addressobject",
            name="role",
        ),
        migrations.RemoveField(
            model_name="addressobjectgroup",
            name="role",
        ),
        migrations.RemoveField(
            model_name="addresspolicyobject",
            name="role",
        ),
        migrations.RemoveField(
            model_name="fqdn",
            name="role",
        ),
        migrations.RemoveField(
            model_name="iprange",
            name="role",
        ),
        migrations.RemoveField(
            model_name="policy",
            name="role",
        ),
        migrations.RemoveField(
            model_name="policyrule",
            name="role",
        ),
        migrations.RemoveField(
            model_name="serviceobject",
            name="role",
        ),
        migrations.RemoveField(
            model_name="serviceobjectgroup",
            name="role",
        ),
        migrations.RemoveField(
            model_name="servicepolicyobject",
            name="role",
        ),
        migrations.RemoveField(
            model_name="sourcedestination",
            name="role",
        ),
        migrations.RemoveField(
            model_name="userobject",
            name="role",
        ),
        migrations.RemoveField(
            model_name="userobjectgroup",
            name="role",
        ),
        migrations.RemoveField(
            model_name="userpolicyobject",
            name="role",
        ),
        migrations.RemoveField(
            model_name="zone",
            name="role",
        ),
        migrations.DeleteModel(
            name="Role",
        ),
    ]