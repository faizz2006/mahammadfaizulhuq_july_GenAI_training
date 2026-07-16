# q3_shopping_cart.py

# ---------------- Part A ----------------

print("Part A: Mutable Default Argument Bug")

def add_item(item, cart=[]):
    cart.append(item)
    return cart

print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", cart=["bread"]))
print(add_item("eggs"))

print("\n")


# ---------------- Part B ----------------

print("Part B: Fixed Version")

def add_item_fixed(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart

print(add_item_fixed("apple"))
print(add_item_fixed("banana"))
print("\n")


# ---------------- Part C ----------------

def create_cart(owner, discount=0):
    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }


def add_to_cart(cart, name, price, qty=1):
    cart["items"].append({
        "name": name,
        "price": price,
        "qty": qty
    })


def calculate_total(cart):
    total = 0

    for item in cart["items"]:
        total += item["price"] * item["qty"]

    discount = cart["discount"]

    final = total - (total * discount / 100)

    return final


def update_price(price_tuple, new_price):
    try:
        price_tuple[0] = new_price
    except TypeError:
        print("Tuple is immutable. Cannot modify tuple elements.")


cart1 = create_cart("Faiz", 10)
cart2 = create_cart("Rahul", 5)

add_to_cart(cart1, "Laptop", 50000, 1)
add_to_cart(cart1, "Mouse", 500, 2)

add_to_cart(cart2, "Phone", 30000, 1)
add_to_cart(cart2, "Headphones", 2000, 1)

print("Cart 1")
print(cart1)
print("Total:", calculate_total(cart1))

print()

print("Cart 2")
print(cart2)
print("Total:", calculate_total(cart2))

print()

price = (5000,)
update_price(price, 6000)

"""
Discussion Answers

1. discount=0 is safe because integers are immutable.
   cart=[] is dangerous because lists are mutable.

2. Rebinding changes the variable reference.
   Mutating changes the existing object.

3. Mutable:
   list
   dict
   set

   Immutable:
   tuple
   str
   int

4. Yes.
   Lists are mutable, so changes made inside functions
   are reflected outside the function.
"""