# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Customer:
    def __init__(self, customer_id, name, email, contact, address):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.contact = contact
        self.address = address
        self.orders = []  # List to store orders placed by the customer

    def placeOrder(self, order):
        """
        Function to place an order.
        Adds the order to the customer's order list.
        """
        self.orders.append(order)
        print(f"Order {order.order_id} placed successfully by {self.name}.")

    def trackStatus(self, order_id):
        """
        Function to track the status of an order.
        """
        for order in self.orders:
            if order.order_id == order_id:
                print(f"Order {order_id} status: {order.status}")
                return
        print(f"Order {order_id} not found.")

    def viewOrders(self):
        """
        Function to view all orders placed by the customer.
        """
        if not self.orders:
            print("No orders found.")
        else:
            print(f"Orders placed by {self.name}:")
            for order in self.orders:
                print(f"Order ID: {order.order_id}, Delivery Date: {order.delivery_date}, Status: {order.status}")


class Order:
    def __init__(self, order_id, customer_id, delivery_date, delivery_method, total_weight, items):
        self.order_id = order_id
        self.customer_id = customer_id
        self.delivery_date = delivery_date
        self.delivery_method = delivery_method
        self.total_weight = total_weight
        self.items = items
        self.status = "Pending"  # Default status

    def createOrder(self):
        """
        Function to create an order.
        """
        self.status = "Created"
        print(f"Order {self.order_id} created successfully.")

    def updateStatus(self, new_status):
        """
        Function to update the status of an order.
        """
        self.status = new_status
        print(f"Order {self.order_id} status updated to: {self.status}")


class DeliveryNote:
    def __init__(self, note_id, order_id, delivery_date, total_price):
        self.note_id = note_id
        self.order_id = order_id
        self.delivery_date = delivery_date
        self.total_price = total_price

    def generateNote(self):
        """
        Function to generate a delivery note.
        """
        print("\n--- Delivery Note ---")
        print(f"Note ID: {self.note_id}")
        print(f"Order ID: {self.order_id}")
        print(f"Delivery Date: {self.delivery_date}")
        print(f"Total Price: {self.total_price}")
        print("---------------------\n")


class DeliveryStaff:
    def __init__(self, staff_id, name, contact):
        self.staff_id = staff_id
        self.name = name
        self.contact = contact
        self.assigned_orders = []  # List to store orders assigned to the staff

    def assignOrder(self, order):
        """
        Function to assign an order to delivery staff.
        """
        self.assigned_orders.append(order)
        order.updateStatus("Assigned to Delivery Staff")
        print(f"Order {order.order_id} assigned to {self.name}.")

    def updateStatus(self, order_id, new_status):
        """
        Function to update the status of an assigned order.
        """
        for order in self.assigned_orders:
            if order.order_id == order_id:
                order.updateStatus(new_status)
                return
        print(f"Order {order_id} not found in assigned orders.")

    def viewAssignedOrders(self):
        """
        Function to view all orders assigned to the delivery staff.
        """
        if not self.assigned_orders:
            print("No orders assigned.")
        else:
            print(f"Orders assigned to {self.name}:")
            for order in self.assigned_orders:
                print(f"Order ID: {order.order_id}, Status: {order.status}")


# Create Customer object
customer = Customer("CUST001", "Sarah Johnson", "sarah.johnson@example.com", "+971123456789", "45 Knowledge Avenue, Dubai, UAE")

# Create Order object
order = Order("DEL123456789", "CUST001", "2025-01-25", "Courier", "7 kg", ["Wireless Keyboard", "Wireless Mouse & Pad Set", "Laptop Cooling Pad", "Camera Lock"])

# Create DeliveryNote object
delivery_note = DeliveryNote("DN-2025-001", "DEL123456789", "2025-01-25", "AED 283.50")

# Create DeliveryStaff object
delivery_staff = DeliveryStaff("STAFF001", "John Doe", "+971987654321")

# Place the order
customer.placeOrder(order)

# Create the order
order.createOrder()

# Assign the order to delivery staff
delivery_staff.assignOrder(order)

# Update the order status
delivery_staff.updateStatus("DEL123456789", "Out for Delivery")

# Generate the delivery note
delivery_note.generateNote()

# Track the order status
customer.trackStatus("DEL123456789")

# View all orders placed by the customer
customer.viewOrders()

# View all orders assigned to the delivery staff
delivery_staff.viewAssignedOrders()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # This block will execute when the script is run directly
    print("Running the delivery management system...")
