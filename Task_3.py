from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    
    days_of_week = {
        "Monday": '',
        "Tuesday": '',
        "Wednesday": '',
        "Thursday": '',
        "Friday": '',
    }
    now = datetime.now()
    now7 = now + timedelta(days=7)

    for i in users:
        for key, value in i.items():
            if isinstance(value, datetime):
                correct_value = value.replace(year=datetime.now().year)
                weekday_name = correct_value.strftime("%A")
                wd = correct_value.weekday()
                if now <= correct_value <= now7: 
                    if 0 <= wd <= 4:
                        days_of_week[weekday_name] += i.get('name')+', '
                    else:
                        days_of_week['Monday'] += i.get('name')+', '
    
    for day,name in days_of_week.items():
        if name:
            new_name = name.rstrip(', ')
            print(f'{day}: {new_name}')
    return days_of_week


get_birthdays_per_week([
    {'name': 'Alice', 'birthday': datetime(1990, 5, 13)},
    {'name': 'Bob', 'birthday': datetime(1995, 5, 10)},
    {'name': 'Sandy', 'birthday': datetime(1995, 5, 10)},
    {'name': 'Charlie', 'birthday': datetime(1985, 5, 8)},
    {'name': 'Abbey', 'birthday': datetime(1993, 9, 7)},
    {'name': 'Eddie', 'birthday': datetime(1994, 3, 22)}
])