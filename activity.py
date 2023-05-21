product_catalog = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}

flat_10_discount = 10
bulk_5_discount = 0.05
bulk_10_discount = 0.1
tiered_50_discount = 0.5

gift_wrap_fee = 1
shipping_fee = 5
max_units_per_package = 10

product_quantities = {}
product_gift_wraps = {}

for product_name in product_catalog:
    quantity = int(input("Enter the quantity of " + product_name + ": "))
    product_quantities[product_name] = quantity
    gift_wrap = input("Would you like to gift wrap " + product_name + "? (y/n): ")
    if gift_wrap.lower() == "y":
        product_gift_wraps[product_name] = True
    else:
        product_gift_wraps[product_name] = False

subtotal = 0

for product_name in product_catalog:
    quantity = product_quantities[product_name]
    price = product_catalog[product_name]
    total_price = quantity * price
    if quantity > 10:
        total_price = total_price - (total_price * bulk_5_discount)
    if quantity > 20:
        total_price = total_price - (total_price * bulk_10_discount)
    if quantity > 30 and product_quantities[product_name] > 15:
        total_price = (price * 15) + ((quantity - 15) * (price * tiered_50_discount))
    subtotal += total_price
    print(product_name + " x " + str(quantity) + " = " + str(total_price))

discount_name = ""
discount_amount = 0

if subtotal > 200:
    discount_name = "flat_10_discount"
    discount_amount = flat_10_discount
elif product_quantities["Product A"] > 10:
    discount_name = "bulk_5_discount"
    discount_amount = bulk_5_discount
elif subtotal > 20:
    discount_name = "bulk_10_discount"
    discount_amount = bulk_10_discount
elif product_quantities["Product A"] > 15:
    discount_name = "tiered_50_discount"
    discount_amount = tiered_50_discount

discount = subtotal * discount_amount
subtotal = subtotal - discount