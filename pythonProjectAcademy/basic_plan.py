from plan import Plan

class BasicPlan(Plan):
    """Class representing a basic plan."""

    def watch_movie(self, movie: str):
        """Watch a movie in the basic plan.

        Args:
            movie (str): The movie to be watched.
        """
        print(f'Watching movie: {movie}')