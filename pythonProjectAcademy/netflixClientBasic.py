from abc import ABC, abstractmethod


class Plan(ABC):
    """Base abstract class representing a plan."""

    @abstractmethod
    def watch_movie(self, movie: str):
        """Abstract method to watch a movie according to the plan.

        Args:
            movie (str): The movie to be watched.
        """
        pass


class BasicPlan(Plan):
    """Class representing a basic plan."""

    def watch_movie(self, movie: str):
        """Watch a movie in the basic plan.

        Args:
            movie (str): The movie to be watched.
        """
        print(f'Watching movie: {movie}')


class PremiumPlan(Plan):
    """Class representing a premium plan."""

    def watch_movie(self, movie: str):
        """Watch a movie in the premium plan.

        Args:
            movie (str): The movie to be watched.
        """
        print(f'Watching movie: {movie} in HD')


class PlanValidator:
    """Class responsible for validating plans."""

    @staticmethod
    def is_valid_plan(plan: str) -> bool:
        """Check if a plan is valid.

        Args:
            plan (str): The plan to be validated.

        Returns:
            bool: True if the plan is valid, False otherwise.
        """
        return plan in ['Basic', 'Premium']


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


# Usage of the code
basic_plan = BasicPlan()
premium_plan = PremiumPlan()

# Creating a client with the basic plan
client = Client('John Doe', 'john@example.com', basic_plan)
client.watch_movie('Movie A', 'Basic')

# Changing the client's plan to the premium plan
client.change_plan(premium_plan)
client.watch_movie('Movie B', 'Premium')
