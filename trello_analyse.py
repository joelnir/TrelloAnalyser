import sys
from file_reader import get_json
import trello_data

args = sys.argv

if len(args) < 2:
    #only script name
    exit("No argument")

json_file = args[1]
data = get_json(json_file)

#print(data["actions"])
print(trello_data.get_weektime_stats(data))
