from django.test import TestCase

from Restaurant.models import Menu


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="1", price=1, inventory=1)
        Menu.objects.create(title="2", price=2, inventory=2)
        Menu.objects.create(title="3", price=3, inventory=3)

    def test_getall(self):
        items = Menu.objects.all()
        self.assertEqual(3, len(items))
