from cal import index


def print_menu(menu_options):
    print('Menu:')
    for option in menu_options:
        print(f'({option[0]}) {option}')
    print('')


def get_inputs(titles):
    if type(titles) == str:
        user_input = input(f'{titles}: ')
        try:
            user_input = int(user_input)
        except:
            pass
        finally:
            return user_input
    else:
        inputs = []
        for title in titles:
            user_input = input(f'{title}: ')
            try:
                user_input = int(user_input)
            except:
                pass
            finally:
                inputs.append(user_input)
        return inputs
