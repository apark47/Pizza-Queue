# testFile.py

from Pizza import Pizza
from SpecialtyPizza import SpecialtyPizza
from CustomPizza import CustomPizza
from PizzaOrder import PizzaOrder
from OrderQueue import OrderQueue
from OrderQueue import QueueEmptyException
import pytest

def test_custom():
    cp1 = CustomPizza("M")
    assert cp1.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: M\n\
Toppings:\n\
Price: $10.00\n"
    cp1.addTopping("pepperoni")
    assert cp1.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: M\n\
Toppings:\n\
\t+ pepperoni\n\
Price: $10.75\n"



    cp2 = CustomPizza("L")
    assert cp2.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: L\n\
Toppings:\n\
Price: $12.00\n"
    cp2.addTopping("mushrooms")
    cp2.addTopping("banana peppers")
    assert cp2.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: L\n\
Toppings:\n\
\t+ mushrooms\n\
\t+ banana peppers\n\
Price: $14.00\n"




    cp3 = CustomPizza("S")
    assert cp3.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
Price: $8.00\n"
    cp3.addTopping("mushrooms")
    cp3.addTopping("banana peppers")
    cp3.addTopping("pepperoni")
    assert cp3.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ mushrooms\n\
\t+ banana peppers\n\
\t+ pepperoni\n\
Price: $9.50\n"


def test_specialty():

    sp1 = SpecialtyPizza("M", "Margarita")
    assert sp1.getPizzaDetails() == \
"SPECIALTY PIZZA\n\
Size: M\n\
Name: Margarita\n\
Price: $14.00\n"

    sp2 = SpecialtyPizza("S", "Extra Cheesy")
    assert sp2.getPizzaDetails() == \
"SPECIALTY PIZZA\n\
Size: S\n\
Name: Extra Cheesy\n\
Price: $12.00\n"

    sp3 = SpecialtyPizza("L", "Santa Barbara Pie")
    assert sp3.getPizzaDetails() == \
"SPECIALTY PIZZA\n\
Size: L\n\
Name: Santa Barbara Pie\n\
Price: $16.00\n"

    

def test_pizza_order():
    cp1 = CustomPizza("M")
    cp1.addTopping("pepperoni")
    cp2 = CustomPizza("L")
    cp2.addTopping("mushrooms")
    cp2.addTopping("banana peppers")
    cp3 = CustomPizza("S")


    sp1 = SpecialtyPizza("M", "Margarita")
    sp2 = SpecialtyPizza("S", "Extra Cheesy")
    sp3 = SpecialtyPizza("L", "Santa Barbara Pie")
  



    order = PizzaOrder(93000) #9:30:00AM
    order.addPizza(cp1)
    order.addPizza(sp1)

    assert order.getOrderDescription() == \
"******\n\
Order Time: 93000\n\
CUSTOM PIZZA\n\
Size: M\n\
Toppings:\n\
\t+ pepperoni\n\
Price: $10.75\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: M\n\
Name: Margarita\n\
Price: $14.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $24.75\n\
******\n"

    order2 = PizzaOrder(130000) #2:00:00PM
    order2.addPizza(cp2)
    order2.addPizza(sp2)

    assert order2.getOrderDescription() == \
"******\n\
Order Time: 130000\n\
CUSTOM PIZZA\n\
Size: L\n\
Toppings:\n\
\t+ mushrooms\n\
\t+ banana peppers\n\
Price: $14.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Extra Cheesy\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $26.00\n\
******\n"


    order3 = PizzaOrder(194500) #7:45:00PM
    order3.addPizza(cp3)
    order3.addPizza(sp3)

    assert order3.getOrderDescription() == \
"******\n\
Order Time: 194500\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
Price: $8.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: L\n\
Name: Santa Barbara Pie\n\
Price: $16.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $24.00\n\
******\n"


def test_OrderQueue():
    cp1 = CustomPizza("M")
    cp1.addTopping("pepperoni")
    cp2 = CustomPizza("L")
    cp2.addTopping("mushrooms")
    cp2.addTopping("banana peppers")
    cp3 = CustomPizza("S")


    sp1 = SpecialtyPizza("M", "Margarita")
    sp2 = SpecialtyPizza("S", "Extra Cheesy")
    sp3 = SpecialtyPizza("L", "Santa Barbara Pie")
  


    order = PizzaOrder(93000) #9:30:00AM
    order.addPizza(cp1)
    order.addPizza(sp1)


    order2 = PizzaOrder(130000) #2:00:00PM
    order2.addPizza(cp2)
    order2.addPizza(sp2)

    order3 = PizzaOrder(194500) #7:45:00PM
    order3.addPizza(cp3)
    order3.addPizza(sp3)
    

    bh = OrderQueue()
    bh.addOrder(order)
    bh.addOrder(order2)
    bh.addOrder(order3)

    assert bh.heapList[1].getTime() == 93000
    assert bh.processNextOrder() == \
"******\n\
Order Time: 93000\n\
CUSTOM PIZZA\n\
Size: M\n\
Toppings:\n\
\t+ pepperoni\n\
Price: $10.75\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: M\n\
Name: Margarita\n\
Price: $14.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $24.75\n\
******\n"

    assert bh.heapList[1].getTime() == 130000
    assert bh.processNextOrder() == \
"******\n\
Order Time: 130000\n\
CUSTOM PIZZA\n\
Size: L\n\
Toppings:\n\
\t+ mushrooms\n\
\t+ banana peppers\n\
Price: $14.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Extra Cheesy\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $26.00\n\
******\n"

    assert bh.heapList[1].getTime() == 194500
    assert bh.processNextOrder() == \
"******\n\
Order Time: 194500\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
Price: $8.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: L\n\
Name: Santa Barbara Pie\n\
Price: $16.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $24.00\n\
******\n"

def test_QueueEmptyException():
    bh = OrderQueue()

    with pytest.raises(QueueEmptyException):
        bh.processNextOrder()

