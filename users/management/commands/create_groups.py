from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Создаёт группы User и Moder"

    def handle(self, *args, **kwargs):
        Group.objects.get_or_create(name="User")
        Group.objects.get_or_create(name="Moder")
        self.stdout.write(self.style.SUCCESS("Группы успешно созданы"))
