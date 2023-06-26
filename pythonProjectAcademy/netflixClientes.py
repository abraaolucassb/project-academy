class Client:
    def __init__(self, name, email, plan):
        self.name = name
        self.email = email
        self.plans_list = ['Basic', 'Premium']
        if plan in self.plans_list:
            self.plan = plan
        else:
            raise Exception('Invalid plan!')


    def change_plan(self, new_plan):
        if new_plan in self.plans_list:
            self.plan = new_plan
        else:
            print('Invalid plan!')


    def ver_filme(self, movie, movie_plan):
        if self.plan == movie_plan:
            print(f'Watch Movie: {movie}')
        elif self.plan == 'Premium':
            print(f'Watch Movie: {movie}')
        elif self.plan == 'Basic' and movie_plan == 'Premium':
            print('Upgrade to Premium to see this movie.')
        else:
            print('Invalid plan!')


client_test = Client('luke', 'luke@gmail.com', 'Basic')
print(client_test.plan)
client_test.ver_filme('Batman', 'Premium')


client_test.change_plan('Premium')
print(client_test.plan)
client_test.ver_filme('Batman', 'Premium')