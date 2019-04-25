import ui
import sys


def main():
    menu_options = ['schedule a new meeting',
                    'cancel an existing meeting',
                    'quit']
    schedule = []

    while True:
        ui.print_schedule(schedule)
        ui.print_menu(menu_options)
        input_ = ui.get_inputs('Your choice')

        if input_ == 's':
            schedule = schedule_new(schedule)
        elif input_ == 'c':
            cancel_existing()
        elif input_ == 'q':
            sys.exit()


if __name__ == "__main__":
    main()
