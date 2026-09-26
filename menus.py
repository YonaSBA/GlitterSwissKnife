def get_choice():
    menus = [like_menu, comment_menu, wow_menu, publish_glit_menu, register_menu, search_menu, update_settings_menu, special_menu]

    while True:
        try:
            main_choice, choices_range = main_menu()
        except ValueError:
            print('\nWrong choice, please try again.')
            continue
        if main_choice == 0:
            return main_choice
        if main_choice in range(1, choices_range):
            while True:
                try:
                    second_choice, choices_range = menus[main_choice - 1]()
                except ValueError:
                    print('\nWrong choice, please try again.')
                    continue
                if second_choice == 0:
                    break
                if second_choice in range(1, choices_range):
                    return [main_choice, second_choice]
                else:
                    print('\nWrong choice, please try again.')
        else:
            print('\nWrong choice, please try again.')


def main_menu():
    print('\nMenu:')
    print('\t0 - Exit.')
    print('\t1 - Like.')
    print('\t2 - Comment.')
    print('\t3 - Wow.')
    print('\t4 - Glit.')
    print('\t5 - Register.')
    print('\t6 - Search.')
    print('\t7 - Settings.')
    print('\t8 - Special.')
    return int(input('Please enter your choice: ')), 9


def like_menu():
    print('\nLike menu:')
    print('\t0 - Return to main menu.')
    print('\t1 - Like a non-existent glit.')
    print('\t2 - Like a glit without access.')
    print('\t3 - Like a glit with a screen name of fewer than 5 characters (unknown).')
    print('\t4 - Like a glit twice.')
    print('\t5 - Unlike another user\'s like.')
    print('\t6 - Expose a glit ID by liking it.')
    return int(input('Please enter your choice: ')), 7


def comment_menu():
    print('\nComment menu:')
    print('\t0 - Return to main menu.')
    print('\t1 - Comment on a non-existent glit.')
    print('\t2 - Comment on a glit without access.')
    print('\t3 - Comment on a glit with a screen name of fewer than 5 characters (unknown).')
    print('\t4 - Comment on a glit with empty content [PATCHED].')
    print('\t5 - Comment on a glit with content longer than 140 characters.')
    print('\t6 - Comment on a glit in the past.')
    print('\t7 - Comment on a glit in the future.')
    print('\t8 - Comment on a glit with injected HTML code.')
    print('\t9 - Expose a glit ID by commenting on it.')
    return int(input('Please enter your choice: ')), 10


def wow_menu():
    print('\nWow menu:')
    print('\t0 - Return to main menu.')
    print('\t1 - Wow a non-existent glit.')
    print('\t2 - Wow a glit without access.')
    print('\t3 - Wow a glit with a screen name of fewer than 5 characters (unknown).')
    print('\t4 - Wow a glit twice.')
    print('\t5 - Unwow another user\'s wow.')
    print('\t6 - Expose a glit ID by wowing it.')
    return int(input('Please enter your choice: ')), 7


def publish_glit_menu():
    print('\nPublish glit menu:')
    print('\t0 - Return to main menu.')
    print('\t1 - Publish a glit in another user\'s feed without access.')
    print('\t2 - Publish a glit with a screen name of fewer than 5 characters (unknown) in another user\'s feed.')
    print('\t3 - Publish an empty glit [PATCHED].')
    print('\t4 - Publish a glit longer than 140 characters.')
    print('\t5 - Publish a glit in the past.')
    print('\t6 - Publish a glit in the future.')
    print('\t7 - Publish a glit with injected HTML code.')
    print('\t8 - Publish a glit and change the user avatar.')
    print('\t9 - Publish a glit with an unknown font color.')
    print('\t10 - Publish a glit with an unknown background color.')
    return int(input('Please enter your choice: ')), 11


def register_menu():
    print('\nRegister menu:')
    print('\t0 - Return to main menu.')
    print('\t1 - Register with a registration code of fewer than 5 characters.')
    print('\t2 - Register with a screen name of fewer than 5 characters [PATCHED].')
    print('\t3 - Register with a username of fewer than 5 characters [PATCHED].')
    print('\t4 - Register with an empty email address [PATCHED].')
    return int(input('Please enter your choice: ')), 5


def search_menu():
    print('\nSearch menu:')
    print('\t0 - Return to main menu.')
    print('\t1 - Perform an empty search.')
    print('\t2 - Expose a user ID and email address by searching for their screen name.')
    return int(input('Please enter your choice: ')), 3


def update_settings_menu():
    print('\nUpdate settings menu:')
    print('\t0 - Return to main menu.')
    print('\t1 - Update a user\'s screen name to fewer than 5 characters [PATCHED].')
    print('\t2 - Expose a user\'s username via their ID.')
    return int(input('Please enter your choice: ')), 3


def special_menu():
    print('\nSpecial menu:')
    print('\t0 - Return to main menu.')
    print('\t1 - Expose a user\'s password checksum via their screen name.')
    return int(input('Please enter your choice: ')), 2
