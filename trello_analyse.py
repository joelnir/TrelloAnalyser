import sys
from file_reader import get_json

args = sys.argv

if len(args) < 2:
    #only script name
    exit("No argument")

json_file = args[1]
trello_data = get_json(json_file)

print(trello_data)
