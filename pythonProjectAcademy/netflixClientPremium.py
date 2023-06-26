class ClientData:
    def __init__(self, name: str, email: str, plan: str):
        self.name = name
        self.email = email
        self.plan = plan


class ClientPlanValidator:
    def __init__(self):
        self.plans_list = ['Basic', 'Premium']

    def is_valid_plan(self, plan):
        return plan in self.plans_list


class Client:
    def __init__(self, client_data, plan_validator):
        self.client_data = client_data
        self.plan_validator = plan_validator

    def change_plan(self, new_plan):
        if self.plan_validator.is_valid_plan(new_plan):
            self.client_data.plan = new_plan
        else:
            print('Invalid plan!')

    def watch_movie(self, movie, movie_plan):
        if self.client_data.plan == movie_plan:
            print(f'Watch Movie: {movie}')
        elif self.client_data.plan == 'Premium':
            print(f'Watch Movie: {movie}')
        elif self.client_data.plan == 'Basic' and movie_plan == 'Premium':
            print('Upgrade to Premium to see this movie.')
        else:
            print('Invalid plan!')


# Exemplo de uso:
client_data = ClientData('Luke', 'luke@gmail.com', 'Basic')
plan_validator = ClientPlanValidator()

client = Client(client_data, plan_validator)

print(client.client_data.plan)
client.watch_movie('Batman', 'Premium')

client.change_plan('Premium')
print(client.client_data.plan)
client.watch_movie('Batman', 'Premium')
