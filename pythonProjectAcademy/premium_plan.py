from plan import Plan

class PremiumPlan(Plan):
    """Class representing a premium plan."""

    def watch_movie(self, movie: str):
        """Watch a movie in the premium plan.

        Args:
            movie (str): The movie to be watched.
        """
        print(f'Watching movie: {movie} in HD')