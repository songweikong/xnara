from rest_framework.test import APITestCase
from requests import patch

from xnara.xnara.models import Customer

# Create your tests here.


# unit test for customer model
class CustomerModelTest(APITestCase):
    customer_id = 101

    mocked_pack1_data = [{"customer_id":101,"pack_data":[{"ingredient":"Calcium carbonate","inventory_code":"MINCAC","quantity":40,"unit":"mg"},{"ingredient":"Ferric pyrophosphate","inventory_code":"MINFEP","quantity":15.6,"unit":"mg"},{"ingredient":"Biotin (B7)","inventory_code":"VITB7","quantity":30,"unit":"mcg"}],"id":"1"},{"customer_id":102,"pack_data":[{"ingredient":"Tocopherol as Vitamin E Acetate","inventory_code":"VITET","quantity":10.4,"unit":"mg"},{"ingredient":"Vitamin D as Ergocalciferol","inventory_code":"VITDE","quantity":15,"unit":"mcg"}],"id":"2"},{"customer_id":103,"pack_data":[{"ingredient":"Calcium carbonate","inventory_code":"MINCAC","quantity":40,"unit":"mg"},{"ingredient":"Ferric pyrophosphate","inventory_code":"MINFEP","quantity":10.2,"unit":"mg"},{"ingredient":"Biotin (B7)","inventory_code":"VITB7","quantity":30,"unit":"mcg"}],"id":"3"},{"customer_id":104,"pack_data":[{"ingredient":"Tocopherol as Vitamin E Acetate","inventory_code":"VITET","quantity":10.4,"unit":"mg"},{"ingredient":"Vitamin D as Ergocalciferol","inventory_code":"VITDE","quantity":15,"unit":"mcg"}],"id":"4"}]

    mocked_pack2_data = [{"customer_id":101,"pack_data":[{"inventory_code":"PRCHLPF19","ingredient":"Lactobacillus paracasei F-19","quantity":1,"unit":"B cfu"},{"inventory_code":"PRCHLC431","ingredient":"Lactobacillus casei 431","quantity":10,"unit":"B cfu"}],"id":"1"},{"customer_id":102,"pack_data":[{"inventory_code":"PRCHLPF19","ingredient":"Lactobacillus paracasei F-19","quantity":2,"unit":"B cfu"},{"inventory_code":"PRCHLC431","ingredient":"Lactobacillus casei 431","quantity":20,"unit":"B cfu"}],"id":"2"},{"customer_id":103,"pack_data":[{"inventory_code":"PRCHLPF19","ingredient":"Lactobacillus paracasei F-19","quantity":3,"unit":"B cfu"},{"inventory_code":"PRCHLC431","ingredient":"Lactobacillus casei 431","quantity":30,"unit":"B cfu"}],"id":"3"},{"customer_id":104,"pack_data":[{"inventory_code":"PRCHLPF19","ingredient":"Lactobacillus paracasei F-19","quantity":4,"unit":"B cfu"},{"inventory_code":"PRCHLC431","ingredient":"Lactobacillus casei 431","quantity":40,"unit":"B cfu"}],"id":"4"}]
    
    # test for get_order method
    def test_get_order(self):
        # create customer object
        customer = Customer(customer_id=self.customer_id)
        # mock requests response with mocked data for both pack 1 and pack 2 calls
        with patch('requests.get') as mocked_get:
            mocked_get.side_effect = [self.mocked_pack1_data, self.mocked_pack2_data]
            # get order
            customer.get_order()
            # check if order is retrieved
            self.assertIsNotNone(customer.p1)
            self.assertIsNotNone(customer.p2)


    # test for get_formatted_data method
    def test_get_formatted_data(self):
        with patch('requests.get') as mocked_get:
            mocked_get.side_effect = [self.mocked_pack1_data, self.mocked_pack2_data]
            # get order
            # create customer object
            customer = Customer(customer_id=self.customer_id)
            # get order
            customer.get_order()
            # get formatted data
            data = customer.get_formatted_data()
            # check if data is formatted correctly
            self.assertEqual(data['customer_id'], self.customer_id)
            self.assertEqual(data['pack1'], customer.p1)
            self.assertEqual(data['pack2'], customer.p2)
            self.assertEqual(data['id'], customer.p1['id'])
