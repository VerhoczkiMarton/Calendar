def import_from_file(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            meetings = []
            for line in lines:
                splitted_line = line.strip().split(',')
                for index in range(len(splitted_line)):
                    try:
                        splitted_line[index] = int(splitted_line[index])
                    except:
                        continue
                meetings.append(splitted_line)
            return meetings
    except:
        return []


def export_to_file(schedule, filename):
    with open(filename, 'w') as f:
        for meeting in schedule:
            f.write(f'{meeting[0]},{meeting[1]},{meeting[2]}\n')
