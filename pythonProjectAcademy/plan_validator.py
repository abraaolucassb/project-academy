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