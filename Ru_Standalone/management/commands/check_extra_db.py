from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError

class Command(BaseCommand):
    help = 'Check if the connection to the extra database works'

    def handle(self, *args, **kwargs):
        db_conn = connections['default']
        db_conn2 = connections['Ru']
        self.stdout.write(self.style.SUCCESS(db_conn))
        self.stdout.write(self.style.SUCCESS(db_conn2))
        try:
            db_conn.cursor()
            self.stdout.write(self.style.SUCCESS('Successfully connected to the extra database'))
        except OperationalError:
            self.stdout.write(self.style.ERROR('Failed to connect to the extra database'))