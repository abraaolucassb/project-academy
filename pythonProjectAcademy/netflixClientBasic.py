class ClientPlanValidator:
    """Validates if the client's plan is compatible with the available plans.

    Attributes:
        plans_list (list): List of available plans.

    Methods:
        __init__(): Initializes a new instance of the ClientPlanValidator class.
        is_valid_plan(plan: str) -> bool: Checks if a given plan is valid.
    """
    def __init__(self):
        """Initializes a new instance of the ClientPlanValidator class."""
        self.plans_list = ['Basic', 'Premium']

    def is_valid_plan(self, plan: str):
        """Checks if a given plan is valid.

        Args:
            plan (str): The plan to be validated.

        Returns:
            bool: True if the plan is valid, False otherwise.

        """
        return plan in self.plans_list


class Client:
    """Class that represents a Client with the attributes: name, email, and plan.

    Attributes:
        name (str): The client's name.
        email (str): The client's email address.
        plan (str): The client's plan.

    Methods:
        __init__(name, email, plan): Initializes a new instance of the Client class.
        change_plan(new_plan): Changes the client's plan.
        watch_movie(movie, movie_plan): Simulates that the client is watching a movie.
    """

    def __init__(self, name: str, email: str, plan: str):
        """Initializes a new instance of the Client class.

        Args:
            name (str): The client's name.
            email (str): The client's email.
            plan (str): The client's plan.

        """
        self.name = name
        self.email = email
        self.plan = plan

    def change_plan(self, new_plan: str):
        """Changes the user's plan to another.

        Args:
            new_plan (str): New plan that the user wants.
        """
        plan_validator = ClientPlanValidator()
        if plan_validator.is_valid_plan(new_plan):
            self.plan = new_plan
        else:
            print('Invalid plan!')

    def watch_movie(self, movie: str, movie_plan: str):
        """Watch movie according to the client's plan.

        Args:
            movie (str): Client's favorite movie.
            movie_plan (str): Movie plan.
        """
        if self.plan == movie_plan:
            print(f'Watch Movie: {movie}')
        elif self.plan == 'Premium':
            print(f'Watch Movie: {movie}')
        elif self.plan == 'Basic' and movie_plan == 'Premium':
            print('Upgrade to Premium to see this movie.')
        else:
            print('Invalid plan!')


# Test the Client class.

# Create a new client with a Basic plan.
client_test = Client('luke', 'luke@gmail.com', 'Basic')
print(client_test.plan)

# Try to watch a movie with a different plan.
client_test.watch_movie('Batman', 'Premium')

# Changes the client's plan to Premium.
client_test.change_plan('Premium')
print(client_test.plan)

# Watch a movie with the new plan.
client_test.watch_movie('Batman', 'Premium')
