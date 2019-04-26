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
    while not validate_meeting(schedule, meeting):
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


def validate_meeting(schedule, meeting):
    valid_durations = [1, 2]
    valid_starts = [x for x in range(8, 19)]
    meeting_times_current = get_meeting_times(meeting)
    meeting_times_already = [get_meeting_times(x) for x in schedule]
    overlap = False

    for meeting_time_already in meeting_times_already:
        overlap = get_overlap(meeting_time_already, meeting_times_current)

    if meeting[index('duration')] not in valid_durations:
        ui.print_message('ERROR: Invalid duration.')
        return False
    elif meeting[index('start')] not in valid_starts:
        ui.print_message('ERROR: Meeting is outside of your working hours (8 to 18)!')
        return False
    elif overlap:
        ui.print_message('ERROR: Meeting overlaps with existing meeting!')
        return False
    else:
        return True


def get_meeting_times(meeting):
    meeting_times = []
    meeting_times.append(meeting[index('start')])
    for i in range(meeting[index('duration')]):
        meeting_times.append(meeting_times[i] + 1)
    return meeting_times


def get_overlap(meeting_times_1, meeting_times_2):
    for meeting_time_1 in meeting_times_1:
        if meeting_time_1 in meeting_times_2:
            return True
    return False


if __name__ == "__main__":
    main()
