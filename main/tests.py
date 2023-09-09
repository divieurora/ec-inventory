from django.test import TestCase, Client
from main.models import Item

# Create your tests here.
class mainTest(TestCase):
    # def test_main_url_is_exist(self):
    #     response = Client().get('/main/')
    #     self.assertEqual(response.status_code, 200)

    # def test_main_using_main_template(self):
    #     response = Client().get('/main/')
    #     self.assertTemplateUsed(response, 'main.html')

    def setUp(self):
        Item.objects.create(name="White T-shirt", amount=2, description="Basic H&M White T-shirt", category="Top")
        Item.objects.create(name="Blue Jeans", amount=1, description="Colorbox Baggy Blue Jeans", category="Bottom")

    def test_item_is_exist(self):
        tshirt = Item.objects.get(name="White T-shirt")
        jeans = Item.objects.get(name="Blue Jeans")
        self.assertEqual(tshirt.cat(), "White T-shirt is a Top")
        self.assertEqual(jeans.cat(), "Blue Jeans is a Bottom")