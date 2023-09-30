#----- Advanced Python Decorator Functions -----#

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(func):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            func(args[0])
        else:
            print("Please login first")
    return wrapper

@is_authenticated_decorator
def create_new_blog(user):
    print(f"This is {user.name}'s new blog post")


new_user = User("AliRed")
new_user.is_logged_in = True
create_new_blog(new_user)