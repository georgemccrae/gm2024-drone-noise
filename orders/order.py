from cityMap.citymap import Coordinate
from commons.decorators import auto_str
from commons.enum import OrderStatus
from datetime import datetime


@auto_str
class Order:
    """
    Food delivery orders.
    """
    
    def __init__(self, order_id, start_location: Coordinate, end_location: Coordinate, time: datetime, description=""):
        self.order_id = order_id                # Order id
        self.start_location = start_location    # Start location
        self.end_location = end_location        # End location
        self.generate_time = time               # Generated step
        self.deliver_time = None                # Delivered step
        self.status = None                      # Order's status
        self.description = description          # Order description
        self.generate()
        
    def generate(self):
        """The order is generated by order generator and is waiting for drones to accept"""
        self.status = OrderStatus.WAITING
        # print(f"[{datetime.now()}] Order '{self.order_id}' is created")
    
    def accept(self):
        """The order is accepted by a drone and the drone is heading to the restaurant to pick up order"""
        self.status = OrderStatus.ACCEPTED
        # print(f"[{datetime.now()}] Order '{self.order_id}' is accepted")
    
    def deliver(self):
        """The order is being delivered by a drone"""
        self.status = OrderStatus.DELIVERING
        # print(f"[{datetime.now()}] Order '{self.order_id}' is being delivered")
        
    def complete(self):
        """The order is complete and food is delivered"""
        self.deliver_time = datetime.now()
        self.status = OrderStatus.COMPLETE
        # print(f"[{datetime.now()}] Order '{self.order_id}' is complete")