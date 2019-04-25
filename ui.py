from cal import index


def print_menu(menu_options):
    print('Menu:')
    for option in menu_options:
        print(f'({option[0]}) {option}')
    print('')
