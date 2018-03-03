import sys

from file_reader import get_json
from trello_data import get_weektime_stats
from painter import show_week

args = sys.argv

if len(args) < 2:
    #only script name
    exit("No argument")

json_file = args[1]
data = get_json(json_file)

week_stats = get_weektime_stats(data)

start_color = [0, 0, 0]
stop_color = [255, 0, 0]

show_week(week_stats, start_color, stop_color)
