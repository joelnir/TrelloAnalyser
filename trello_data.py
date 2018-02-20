import datetime

def get_board_name(data):
    return data["name"]

def get_labels(data):
    return [label["name"] for label in data["labels"]]

def get_unique_actions(data):
    actions = data["actions"]

    u_act = []

    for action in actions:
        if(not (action["type"] in u_act)):
            u_act.append(action["type"])

    return u_act

def get_weekday(date_string):
    year = int(date_string[0:4])
    month = int(date_string[5:7])
    day = int(date_string[8:10])

    date = datetime.datetime(year, month, day)
    return date.weekday();

def get_hour_of_day(date_string):
    return date_string[11:13]

def get_weektime_stats(data, filter = 0):
    actions = data["actions"]

    #return actions[0]
    date_times = [action["date"] for action in actions]

    return [(get_hour_of_day(date_string), get_weekday(date_string)) for date_string in date_times]
