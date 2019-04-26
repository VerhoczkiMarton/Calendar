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
            schedule = add_meeting(schedule)
        elif input_ == 'c':
            schedule = cancel_meeting(schedule)
        elif input_ == 'q':
            sys.exit()


def add_meeting(schedule):
    ui.print_message('Schedule a new meeting.')
    meeting = ui.get_inputs(['Enter meeting title',
                             'Enter duration in hours (1 or 2)',
                             'Enter start time'])
    ui.print_message('Meeting added.')
    schedule.append(meeting)
    return schedule


def cancel_meeting(schedule):
    ui.print_message('Cancel an existing meeting.')
    meeting_to_cancel = ui.get_inputs('Enter the start time')
    if meeting_to_cancel in [x[index('start')] for x in schedule]:
        for meeting in schedule:
            if meeting[index('start')] == meeting_to_cancel:
                schedule.remove(meeting)
    else:
        ui.print_message('ERROR: There is no meeting starting at that time!')
    return schedule


def index(name):
    if name == 'title':
        return 0
    elif name == 'duration':
        return 1
    elif name == 'start':
        return 2
    else:
        raise IndexError


if __name__ == "__main__":
    main()
