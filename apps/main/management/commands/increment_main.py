from __future__ import annotations

from argparse import ArgumentParser

from django.core.management.base import BaseCommand
from django.db import DEFAULT_DB_ALIAS
from dynamic_db_router import in_database

from apps.main.models import CountData


class Command(BaseCommand):
    help = "increment main counter"

    def add_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument(
            "-d",
            "--database",
            dest="database",
            type=str,
            required=False,
            help=f"Target database setting name (default={DEFAULT_DB_ALIAS})",
            default=DEFAULT_DB_ALIAS,
        )

    def handle(self, *args: list, **options: dict) -> None:
        db_setting_name = options.get("database", DEFAULT_DB_ALIAS)
        with in_database(db_setting_name, write=True):
            count_data, _ = CountData.objects.get_or_create()
            prev_count = count_data.count
            count_data.count = prev_count + 1
            count_data.save()
            print(f"COUNT(main): {prev_count} -> {count_data.count}")
