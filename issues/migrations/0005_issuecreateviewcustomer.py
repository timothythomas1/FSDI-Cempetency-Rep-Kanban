# Generated by Django 4.1.2 on 2022-10-14 11:48

from django.conf import settings
import django.contrib.auth.mixins
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.views.generic.edit


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_alter_customuser_role"),
        ("issues", "0004_issuecreateview"),
    ]

    operations = [
        migrations.CreateModel(
            name="IssueCreateViewCustomer",
            fields=[
                (
                    "customuser_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            bases=(
                django.contrib.auth.mixins.LoginRequiredMixin,
                django.views.generic.edit.CreateView,
                "accounts.customuser",
            ),
            managers=[("objects", django.contrib.auth.models.UserManager()),],
        ),
    ]
