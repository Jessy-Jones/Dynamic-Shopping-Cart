def add_to_cart(item_name, price, *args, **kwargs):
  """
  Adds an item to the shopping cart.

  Args:
    item_name: The name of the item.
    price: The price of the item.
    *args: Optional discounts as percentages.
    **kwargs: Optional item details (e.g., color, size).

  Returns:
    The final price of the item after applying discounts.
  """
  final_price = price
  for discount in args:
    final_price -= (final_price * discount) / 100
  return final_price

cart = {}  # Dictionary to store items in the cart

while True:
  item_name = input("Enter item name (or 'done' to finish): ")
  if item_name == 'done':
    break

  price = float(input("Enter item price: "))
  discounts = input("Enter discounts (if any, separated by spaces): ").split()
  discounts = [float(d) for d in discounts]
  item_details = input("Enter item details (e.g., color=red size=large): ")

  final_price = add_to_cart(item_name, price, *discounts)

  if item_name in cart:
    print(f"{item_name} already exists in the cart.")
  else:
    cart[item_name] = {'price': final_price, 'details': item_details}
    print(f"Item added: {item_name} - Final Price: ${final_price:.2f}")

print("\n--- Cart Summary ---")
total_cost = 0
for item, details in cart.items():
  print(f"{item} - ${details['price']:.2f} ({details['details']})")
  total_cost += details['price']
print(f"Total Cost: ${total_cost:.2f}")