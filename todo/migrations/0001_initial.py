# Generated by Django 5.1.5 on 2025-02-09 13:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Todo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50, verbose_name="제목")),
                ("description", models.TextField(verbose_name="설명")),
                (
                    "is_completed",
                    models.BooleanField(default=False, verbose_name="완료 여부"),
                ),
                ("start_date", models.DateTimeField(verbose_name="시작 날짜")),
                ("end_date", models.DateTimeField(verbose_name="마감 날짜")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="생성 날짜"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="수정 날짜"),
                ),
                (
                    "completed_image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="todo/completed_images",
                        verbose_name="완료_이미지",
                    ),
                ),
                (
                    "thumbnail",
                    models.ImageField(
                        blank=True,
                        default="todo/no_image/NO-IMAGE.gif",
                        null=True,
                        upload_to="todo/thumbnails",
                        verbose_name="썸네일_이미지",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "할 일",
                "verbose_name_plural": "할 일 목록",
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("message", models.TextField(max_length=200, verbose_name="댓글")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="생성 날짜"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="수정 날짜"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="유저",
                    ),
                ),
                (
                    "todo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="todo.todo",
                        verbose_name="할 일",
                    ),
                ),
            ],
            options={
                "verbose_name": "댓글",
                "verbose_name_plural": "댓글 목록",
            },
        ),
    ]
