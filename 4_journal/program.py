import journal


def main():
    print_header()
    run_event_loop()


def print_header():
    print("Journal App")


def run_event_loop():
    print('What do you want to do with your Journal?')
    cmd = 'Empty'
    journal_name = 'default'
    journal_data = journal.load(journal_name)

    while cmd != 'x' and cmd:
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print("sorry we don't understand '{}'.".format(cmd))

    print('Done, goodbye')
    journal.save(journal_name, journal_data)


def list_entries(data):
    for idx, entry in enumerate(data):
        print('* '
        ''
            '{}: {}'.format(idx + 1, entry))


def add_entry(data):
    text = input('Type your entry, <Enter> to exit: ')
    journal.add_entry(text, data)


main()