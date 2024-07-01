from django.test import TestCase

from Restaurant.models import Menu


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=69, inventory=100)
        self.assertEqual(str(item), "IceCream : 69")
