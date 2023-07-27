from django.db import models
import requests

# Create your models here.

# customer model with fields
class Customer(models.Model):
    # customer_id is primary key
    customer_id = models.AutoField(primary_key=True)

    class Meta:
        app_label = 'xnara'

    def __str__(self):
        return self.customer_id

    # get order from two other apis https://6466e9a7ba7110b663ab51f2.mockapi.io/api/v1/pack1 and https://6466e9a7ba7110b663ab51f2.mockapi.io/api/v1/pack2
    # assumption: customer_id is unique in the pack1 and pack2 apis, so there is 1 or 0 pack data for each customer
    def get_order(self):
        # get data from two apis
        pack1 = requests.get("https://6466e9a7ba7110b663ab51f2.mockapi.io/api/v1/pack1")
        # loop through pack 1 data to get order to get order based on customer_id
        for data in pack1:
            if data['customer_id'] == self.customer_id:
                self.p1 = data
                # stop loop if order is found
                break

        pack2 = requests.get("https://6466e9a7ba7110b663ab51f2.mockapi.io/api/v1/pack2")
        # loop through pack 2 data to get order to get order based on customer_id
        for data in pack2:
            if data['customer_id'] == self.customer_id:
                self.p2 = data
                # stop loop if order is found
                break

    # get formatted data from the retrieved packs
    def get_formatted_data(self):
        self.get_order()
        data = {
            "customer_id": self.customer_id,
        }

        # if pack 1 data exists, add to data in the format of “{ingredient} {quantity}{unit}”
        if self.p1:
            # loop through each item in pack_data to format data. assumption: ingredients, quantity and units are all non-optional fields
            p1_item_list = []
            for item in self.p1["pack_data"]:
                p1_item_list.append(f"{item['ingredient']} {item['quantity']}{item['unit']}")
            data['pack1'] = self.p1
            data['id'] = self.p1['id']
        # if pack 2 data exists, add to data
        if self.p2:
            # loop through each item in pack_data to format data. assumption: ingredients, quantity and units are all non-optional fields
            p2_item_list = []
            for item in self.p2["pack_data"]:
                p2_item_list.append(f"{item['ingredient']} {item['quantity']}{item['unit']}")
            data['pack2'] = p2_item_list
            # assumes that the id is the same for both packs, overwrites if different
            data['id'] = self.p2['id']
        return data