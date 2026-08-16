"""
    The E-Commerce Analytics Pipeline (map, filter, reduce)

Scenario: You have a list of raw transaction dictionaries:

transactions = [
    {"id": 101, "amount": 250.0, "status": "completed", "currency": "USD"},
    {"id": 102, "amount": 0.0,   "status": "pending",   "currency": "USD"},
    {"id": 103, "amount": 180.5, "status": "completed", "currency": "USD"},
    {"id": 104, "amount": 45.0,  "status": "refunded",  "currency": "USD"},
    {"id": 105, "amount": 500.0, "status": "completed", "currency": "USD"},
]
Task: Using only map(), filter(), functools.reduce(), and lambda expressions (no explicit for or while loops):

Filter out all non-"completed" transactions.
Map a 10% tax addition onto the remaining amounts.
Reduce the mapped values into a single net revenue total formatted to 2 decimal places.
"""

from functools import reduce

transactions = [
    {"id": 101, "amount": 250.0, "status": "completed", "currency": "USD"},
    {"id": 102, "amount": 0.0,   "status": "pending",   "currency": "USD"},
    {"id": 103, "amount": 180.5, "status": "completed", "currency": "USD"},
    {"id": 104, "amount": 45.0,  "status": "refunded",  "currency": "USD"},
    {"id": 105, "amount": 500.0, "status": "completed", "currency": "USD"},
]

#filter
non_completed=filter(lambda t:t['status']=="completed",transactions)
print((non_completed))

#map
tax=map(lambda a:a["amount"]*1.10,non_completed)
print((tax))

#reduce
net_revenue = reduce(lambda total, amount: total + amount, tax)

print(f"Net Revenue: ${net_revenue:.2f}")


