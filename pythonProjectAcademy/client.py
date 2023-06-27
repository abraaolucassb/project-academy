from plan import Plan
from plan_validator import PlanValidator

class Client:
    """Class representing a client with a plan."""

    def __init__(self, name: str, email: str, plan: Plan):
        """Initialize a new instance of the Client class.

        Args:
            name (str): The client's name.
            email (str): The client's email.
            plan (Plan): The client's plan.
        """
        self.name = name
        self.email = email
        self.plan = plan

    def change_plan(self, new_plan: Plan):
        """Change the client's plan to a new plan.

        Args:
            new_plan (Plan): The new plan for the client.
        """
        self.plan = new_plan

    def watch_movie(self, movie: str, movie_plan: str):
        """Watch a movie according to the client's plan.

        Args:
            movie (str): The movie to be watched.
            movie_plan (str): The plan associated with the movie.
        """
        if PlanValidator.is_valid_plan(movie_plan):
            self.plan.watch_movie(movie)
        else:
            print('Invalid plan!')