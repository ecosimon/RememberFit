from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    """Come back to this later"""
    help = 'Default command base options'
	
    def add_arguments(self, parser):
        pass
		
    def handle(self, *args, **options):
        pass