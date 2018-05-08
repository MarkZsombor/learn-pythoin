import datetime


def print_header():
    print('------------------------')
    print('       BIRTHDAY')
    print('------------------------')


def get_birthday_from_user():
    print('When were you born?')
    birth_year = int(input('Year [YYYY] '))
    birth_month = int(input('Month [MM] '))
    birth_day = int(input('Day [DD] '))

    bday = datetime.date(birth_year, birth_month, birth_day)
    return bday


def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)
    dt = this_year - target_date
    return dt.days


def print_birthday_info(days):
    if days < 0:
        print('You had your birthday {} days ago'.format(-days))
    elif days > 0:
        print('Your birthday is in {} days'.format(days))
    else:
        print('Happy Birthday')



def main():
    print_header()
    bday = get_birthday_from_user()
    today = datetime.date.today()
    num_days = compute_days_between_dates(bday, today)
    print_birthday_info(num_days)


main()