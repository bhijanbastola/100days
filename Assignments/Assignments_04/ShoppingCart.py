""" 
Problem Statement

We want to build an online shopping cart system that allows users to add products to their cart, calculate the total cost, apply discounts, and generate an invoice. The system should include the following functionalities:

Adding products to the cart
Removing products from the cart
Calculating the total cost
Applying discounts based on user type
Generating an invoice
1. Create the Product class

We create a basic Product class with attributes for the product name and price.

# Your Solution Here
2. Implement the User class

In this step, we create a User class with attributes for the user's name and whether they are a premium member.

# Your Solution Here
3. Create the ShoppingCart class

In this step, we create a ShoppingCart class with methods for adding and removing products from the cart, as well as calculating the total cost of the items in the cart.

Note: Define calculate_total_cost method in the ShoppingCart class, that applies a 10% discount to the total cost if you are premium User.

# Your Solution Here
4. Testing the functionality

Now that we have implemented the necessary classes and methods, let's test our online shopping cart system:


5. Generating Invoice for a given cart
# Your Solution Here
Bonus Challenge

In this case each user share the same cart, which is useless. Also each user can register himself/herself as a premium user, which is not practical again. So, you have to add following two additional features to the above program, to make it more real:

Cart for a user should be independent from other users
Add a new admin feature is_admin that takes in boolean values [True, False], and only admin should be allowed to create other admins and set is_premium=True for other users


"""

class Product:
    def __init__(self, product_name, price):
        self.name = product_name
        self.price = price

    def __str__(self):
        return f"{self.name} - Rs. {self.price:.2f}"


class User:
    def __init__(self, name, is_premium=False, is_admin=False):
        self.name = name
        self.is_premium = is_premium
        self.is_admin = is_admin
        self.cart = ShoppingCart(self)

    def make_premium(self, admin):
        # Only an admin can make another user premium
        if not admin.is_admin:
            raise PermissionError("Only an admin can make users premium.")

        self.is_premium = True
        print(f"{self.name} is now a premium member.")

    def make_admin(self, admin):
        # Only an existing admin can create another admin
        if not admin.is_admin:
            raise PermissionError("Only an admin can create another admin.")

        self.is_admin = True
        print(f"{self.name} is now an admin.")


class ShoppingCart:
    def __init__(self, user):
        self.user = user
        self.items = {}

    def add_product(self, product, quantity=1):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")

        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

        print(f"{quantity} x {product.name} added to cart.")

    def remove_product(self, product, quantity=1):
        if product not in self.items:
            print(f"{product.name} is not in the cart.")
            return

        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")

        if quantity >= self.items[product]:
            del self.items[product]
            print(f"{product.name} removed from cart.")
        else:
            self.items[product] -= quantity
            print(f"{quantity} x {product.name} removed from cart.")

    def calculate_total_cost(self):
        subtotal = 0

        for product, quantity in self.items.items():
            subtotal += product.price * quantity

        discount = 0

        if self.user.is_premium:
            discount = subtotal * 0.10

        total = subtotal - discount

        return subtotal, discount, total

    def invoice(self):
        print("\n" + "=" * 40)
        print("              INVOICE")
        print("=" * 40)

        print(f"Customer: {self.user.name}")
        print(f"Premium Member: {self.user.is_premium}")
        print("-" * 40)

        if not self.items:
            print("Cart is empty.")
            print("=" * 40)
            return

        for product, quantity in self.items.items():
            item_total = product.price * quantity

            print(
                f"{product.name:<15} "
                f"x {quantity:<3} "
                f"Rs. {item_total:.2f}"
            )

        print("-" * 40)

        subtotal, discount, total = self.calculate_total_cost()

        print(f"Subtotal:       Rs. {subtotal:.2f}")
        print(f"Discount:       Rs. {discount:.2f}")
        print(f"Total Cost:     Rs. {total:.2f}")

        print("=" * 40)

# Create products
laptop = Product("Laptop", 100000)
mouse = Product("Mouse", 2000)
keyboard = Product("Keyboard", 5000)

# Create users
admin = User("Admin", is_admin=True)
bhijan = User("Bhijan")
ram = User("Ram")

# Admin makes Bhijan premium
bhijan.make_premium(admin)

# Each user has their own independent cart
bhijan.cart.add_product(laptop, 1)
bhijan.cart.add_product(mouse, 2)
bhijan.cart.add_product(keyboard, 1)

ram.cart.add_product(mouse, 1)

# Remove a product
bhijan.cart.remove_product(mouse, 1)

# Generate invoices
bhijan.cart.invoice()

ram.cart.invoice()