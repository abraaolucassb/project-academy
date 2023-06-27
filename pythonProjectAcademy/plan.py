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