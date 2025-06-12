from django.test import TestCase
from restaurant.views import Menu
from django.core import serializers

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="IceCream2", price=50, inventory=150)
        Menu.objects.create(title="IceCream3", price=30, inventory=200)

    def test_getall(self):
        items = Menu.objects.all()
        self.assertEqual(str(serializers.serialize("json", items)), '[{"model": "restaurant.menu", "pk": 2, "fields": {"title": "IceCream", "price": "80.00", "inventory": 100}}, {"model": "restaurant.menu", "pk": 3, "fields": {"title": "IceCream2", "price": "50.00", "inventory": 150}}, {"model": "restaurant.menu", "pk": 4, "fields": {"title": "IceCream3", "price": "30.00", "inventory": 200}}]')