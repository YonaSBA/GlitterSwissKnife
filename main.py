import menus
import swissknife
import communication
import authentication

ID = 4


def connect():
    primary_sock = communication.build_socket()
    attacked_sock = communication.build_socket()
    general_sock = communication.build_socket()

    users = authentication.set_users()

    return ({'primary': primary_sock, 'attacked': attacked_sock, 'general': general_sock},
            {'primary': authentication.login(primary_sock, users['primary']),
             'attacked': authentication.login(attacked_sock, users['attacked'])})


def disconnect(sockets, users):
    for user in users.keys():
        if users[user] is not None:
            try:
                authentication.logout(sockets[user], users[user][ID])
            except (OSError, KeyError):
                pass

    for socket in sockets.values():
        if socket is not None:
            try:
                socket.close()
            except OSError:
                pass


def main():
    sockets, users = {}, {}
    try:
        sockets, users = connect()
        if users['primary'] is not None and users['attacked'] is not None:
            swissknife.set_sockets_and_users(sockets, users)
            while True:
                choice = menus.get_choice()
                if choice:
                    print('\n' + swissknife.exploit_weakness(choice), end='')
                else:
                    print('\nGoodbye!')
                    break
        else:
            print("\nThe login for one or both users failed, please try again!")
    except KeyboardInterrupt:
        print('\n\nGoodbye!')
    except OSError:
        print('\nNetwork error, please try again!')
    finally:
        disconnect(sockets, users)


if __name__ == "__main__":
    main()
