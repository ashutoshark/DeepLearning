import csv
class Item:
    pay_rate=0.8
    all=[]
    def __init__(self,name:str,price:float,quantity=0):
        # we can run validation for above variables
        assert price >=0,f"Price {price} is not grater than or equal to zero"
        assert quantity>=0,f"Quantity {quantity} is not grater than or equal to zero"
# Assigning to self object
        self.name=name
        self.price=price
        self.quantity=quantity
# action to execute
        Item.all.append(self)
    def calculate_total_price(self):
        return self.price*self.quantity
    
    def apply_discount(self):
        self.price=self.price*self.pay_rate

    @classmethod
    def instatiate_from_csv(cls):
        with open('item.csv','r',-1) as f:
            reader=csv.DictReader(f)
            items=list(reader)
        for item in items:
            # print(item)
            item(
                name=item.get('name'),
                price=item.get('price'),
                quantity=item.get('quantity')
            )

    def __repr__(self):
        return f"Item('{self.name}','{self.price}','{self.quantity}')"

# Item1=Item("phone",100,1)
# Item2=Item("laptop",1000,3)
# Item3=Item("cable",10,5)
# Item4=Item("mouse",50,5)
# Item5=Item("Keyboard",75,5)
# # 
# Item2.pay_rate=0.5 #assing particualr price to particualar items
# Item2.apply_discount() 
# Item3.apply_discount() #it use globle pay_rate as define above           
# print(Item2.price,Item3.price)
Item.instatiate_from_csv()
print(Item.all)