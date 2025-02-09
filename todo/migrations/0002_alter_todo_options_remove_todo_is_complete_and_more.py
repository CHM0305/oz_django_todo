# Generated by Django 5.1.5 on 2025-02-06 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="todo",
            options={"verbose_name": "할 일", "verbose_name_plural": "할 일 목록"},
        ),
        migrations.RemoveField(
            model_name="todo",
            name="is_complete",
        ),
        migrations.RemoveField(
            model_name="todo",
            name="modified_at",
        ),
        migrations.AddField(
            model_name="todo",
            name="is_completed",
            field=models.BooleanField(default=False, verbose_name="완료 여부"),
        ),
        migrations.AddField(
            model_name="todo",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="수정 날짜"),
        ),
        migrations.AlterField(
            model_name="todo",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="생성 날짜"),
        ),
        migrations.AlterField(
            model_name="todo",
            name="description",
            field=models.TextField(verbose_name="설명"),
        ),
        migrations.AlterField(
            model_name="todo",
            name="end_date",
            field=models.DateTimeField(verbose_name="마감 날짜"),
        ),
        migrations.AlterField(
            model_name="todo",
            name="start_date",
            field=models.DateTimeField(verbose_name="시작 날짜"),
        ),
        migrations.AlterField(
            model_name="todo",
            name="title",
            field=models.CharField(max_length=50, verbose_name="제목"),
        ),
    ]
