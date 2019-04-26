import ui
import sys
import storage


def main():
    menu_options = ['schedule a new meeting',
                    'cancel an existing meeting',
                    'edit existing meeting',
                    'display total meeting duration',
                    'reschedule to compact',
                    'quit']

    while True:
        schedule = storage.import_from_file('meetings.txt')
        ui.print_schedule(schedule)
        ui.print_menu(menu_options)
        input_ = ui.get_inputs('Your choice')

        if input_ == 's':
            ui.print_message('Schedule a new meeting.')
            schedule = add_meeting(schedule)
        elif input_ == 'c':
            ui.print_message('Cancel an existing meeting.')
            schedule = cancel_meeting(schedule)
        elif input_ == 'e':
            ui.print_message('Edit an existing meeting.')
            schedule = edit_meeting(schedule)
        elif input_ == 'd':
            ui.print_result(get_total_duration(schedule), 'Total duration of meetings today')
        elif input_ == 'r':
            ui.print_message('Compact schedule.')
            schedule = compact_schedule(schedule)
        elif input_ == 'q':
            sys.exit()
        else:
            ui.print_message('Invalid input')
        storage.export_to_file(schedule, 'meetings.txt')


def add_meeting(schedule):
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
    meeting_to_cancel = ui.get_inputs('Enter the start time')
    if meeting_to_cancel in [x[index('start')] for x in schedule]:
        for meeting in schedule:
            if meeting[index('start')] == meeting_to_cancel:
                schedule.remove(meeting)
    else:
        ui.print_message('ERROR: There is no meeting starting at that time!')
    return schedule


def edit_meeting(schedule):
    meeting_to_edit = ui.get_inputs('Enter the start time')
    if meeting_to_edit in [x[index('start')] for x in schedule]:
        for meeting in schedule:
            if meeting[index('start')] == meeting_to_edit:
                ui.print_message('Editing.')
                schedule.remove(meeting)
                schedule = add_meeting(schedule)
                break
    else:
        ui.print_message('ERROR: There is no meeting starting at that time!')
    return schedule


def get_total_duration(schedule):
    return sum([x[index('duration')] for x in schedule])


def compact_schedule(schedule):
    schedule.sort(key=lambda x: x[index('start')])
    current_time = 8
    for meeting in schedule:
        meeting[index('start')] = current_time
        current_time += meeting[index('duration')]
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
    valid_times = [x for x in range(8, 19)]
    meeting_times_current = get_meeting_times(meeting)
    meeting_times_in_schedule = [get_meeting_times(x) for x in schedule]
    overlap = False

    for meeting_time_in_schedule in meeting_times_in_schedule:
        overlap = get_overlap(meeting_time_in_schedule, meeting_times_current)
        if overlap:
            break

    if meeting[index('duration')] not in valid_durations:
        ui.print_message('ERROR: Invalid duration.')
        return False
    elif meeting[index('start')] not in valid_times:
        ui.print_message('ERROR: Meeting is outside of your working hours (8 to 18)!')
        return False
    elif meeting[index('start')] + meeting[index('duration')] not in valid_times:
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
    meeting_times_1 = set(meeting_times_1)
    if len(meeting_times_1.intersection(meeting_times_2)) > 1:
        return True
    return False


if __name__ == "__main__":
    main()
