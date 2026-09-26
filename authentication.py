import ast
import communication

commands = {100: '100#{{gli&&er}}{{"user_name":"{}","password":"{}","enable_push_notifications":true}}##',
            110: '110#{{gli&&er}}{}##',
            150: '150#{{gli&&er}}{{"registration_code":"{}","user":{{"screen_name":"{}","avatar":"{}","description":"{}","privacy":"{}","id":{},"user_name":"{}","password":"{}","gender":"{}","mail":"{}"}}}}##',
            200: '200#{{gli&&er}}{}##'}


def login(socket, user):
    response = communication.send_and_receive(socket, commands[100].format(user['username'], user['password']))

    if 'Login error' in response:
        return None
    if 'Illegal user login' in response:
        response = communication.send_and_receive(socket, commands[150].format('11111', 'lorem_ipsum', 'im4', 'lorem_ipsum', 'Public', '-1', user['username'], user['password'], 'Male', 'lorem_ipsum@lorem.ipsum'))
        if 'Illegal user registration' in response:
            return None
        communication.send_and_receive(socket, commands[100].format(user['username'], user['password']))

    code = sum(ord(char) for char in user['username'] + user['password'])
    response = communication.send_and_receive(socket, commands[110].format(code))
    return list(ast.literal_eval(response[response.find('}') + 1: -2]).values())


def logout(socket, user):
    communication.send_and_receive(socket, commands[200].format(user))


def set_users():
    users = {'primary': {'username': 'json1', 'password': '1234'}, 'attacked': {'username': 'json2', 'password': '1234'}}

    print('Welcome to the Glitter SwissKnife!')
    print('For the weaknesses we need two users, a primary user and an attacked user.\n')

    if input('Do you want to login as a primary user from your account? yes / any other key: ') == 'yes':
        users['primary'] = {'username': input('Please enter a username: '), 'password': input('Please enter a password: ')}
    else:
        print('The primary user selected is "json1" whose password is "1234".')

    if input('Do you want to login as a attacked user from your account? yes / any other key: ') == 'yes':
        users['attacked'] = {'username': input('Please enter a username: '), 'password': input('Please enter a password: ')}
    else:
        print('The attacked user selected is "json2" whose password is "1234".')

    return users