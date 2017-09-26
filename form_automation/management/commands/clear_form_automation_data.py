from django.core.management.base import BaseCommand
from django.utils import timezone
from form_automation.models import RequestDetails

class Command(BaseCommand):
    def handle(self, *args, **options):
        RequestDetails.objects.filter(request_date<timezone.now()).delete()
        self.stdout.write(self.style.SUCCESS('Successfully Cleaned Database'))
