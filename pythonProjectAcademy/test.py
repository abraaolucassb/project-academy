from basic_plan import BasicPlan
from premium_plan import PremiumPlan
from client import Client

# Usage of the code.
basic_plan = BasicPlan()
premium_plan = PremiumPlan()

# Creating a client with the basic plan.
client = Client('John Doe', 'john@example.com', basic_plan)
client.watch_movie('Movie A', 'Basic')

# Changing the client's plan to the premium plan.
client.change_plan(premium_plan)
client.watch_movie('Movie B', 'Premium')