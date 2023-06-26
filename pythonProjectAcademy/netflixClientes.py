class Client:
    """Class that represents a Client with the attributes: name, email, and plan.

    Attributes:
        name (str): The client's name.
        email (str): The client's email address.
        plans_list (list): List of available plans.
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

        Raises:
            Exception: If the plan entered by the customer is not within the plans_list.
        """
        self.name = name
        self.email = email
        self.plans_list = ['Basic', 'Premium']
        if plan in self.plans_list:
            self.plan = plan
        else:
            raise Exception('Invalid plan!')

    def change_plan(self, new_plan: str):
        """Changes the user's plan to another.

        Args:
            new_plan (str): New plan that the user wants.
        """
        if new_plan in self.plans_list:
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
