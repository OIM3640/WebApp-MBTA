import pprint

with open('stops_mbta.txt', 'rb') as f:
    my_dict = f.read().decode('utf-8')

pprint.pprint(my_dict)
