class User():
    def __init__(a, first_name, last_name, city, age):
        a.first_name = first_name.title()
        a.last_name = last_name.title()
        a.city = city.title()
        a.age = age

    def describe_user(a):
        print("-----")
        print("First Name" + " : " + a.first_name)
        print("Last Name" + " : " + a.last_name)
        print("City" + " : " + a.city)
        print("Age" + " : " + a.age)


def ask_user(message=''):
    user_input = ''
    while not user_input:
        user_input = input(message)
    return user_input


def form_complete(values, placement, length):
    placement = []
    while len(placement) < length:
        first_name = ask_user("Enter First Name: ")
        last_name = ask_user("Enter Last Name: ")
        city = ask_user("Enter City: ")
        age = ask_user("Enter Age: ")
        values = User(first_name, last_name, city, age)
        placement.append(values)
    return placement


if __name__ == '__main__':

    users = form_complete('user', 'users', 3)
    for a in range(len(users)):
        users[a].describe_user()
