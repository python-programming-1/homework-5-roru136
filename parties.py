import csv
import pprint


def get_bar_party_data():
    """this function reads from a csv file and converts the data into a list of dictionaries.
     each item in the list is a dictionary of a specific location and the number of complaint calls
     it received in 2016"""

    bar_list = []
    with open('bar_locations.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            bar_dict = {'location_type': row[0],
                        'zip_code': row[1],
                        'city': row[2],
                        'borough': row[3],
                        'latitude': row[4],
                        'longitude': row[5],
                        'num_calls': row[6]}
            bar_list.append(bar_dict)
    return bar_list


def print_data(data):
    for entry in data:
        print(entry)
        pprint.pprint(entry)
        
def sortVal(val): 
    return val[1]


def get_most_noisy_city_and_borough(data):
    """ fill in the Nones for the dictionary below using the bar party data """
    noisiest_city_and_borough = {'city': None, 'borough': None, 'num_city_calls': None, 'num_borough_calls': None}

    boroughs = set([data[x]['borough'] for x in range(1, len(data))])
    cities = set([data[x]['city'] for x in range(1, len(data))])
    
    borVal = [0] * len(boroughs)
    
    citVal = [0] * len(cities)
    
    for rec in data:
        for idx, val in enumerate(boroughs):
            if rec['borough'] == val:
                borVal[idx] = borVal[idx] + int(rec['num_calls'])
                break
            
    borValSorted = list(zip(boroughs, borVal))
    
    borValSorted.sort(key = sortVal)
    
    #print(borValSorted[-1])
            
    for rec in data:
        for idx, val in enumerate(cities):
            if rec['city'] == val:
                citVal[idx] = citVal[idx] + int(rec['num_calls'])
                break
    
    citValSorted = list(zip(cities, citVal))
    
    citValSorted.sort(key = sortVal)
    
    #print(citValSorted[-1])
    
    noisiest_city_and_borough['city'] = citValSorted[-1][0]
    noisiest_city_and_borough['borough'] = borValSorted[-1][0]
    noisiest_city_and_borough['num_city_calls'] = citValSorted[-1][1]
    noisiest_city_and_borough['num_borough_calls'] = borValSorted[-1][1]
            
    

    return noisiest_city_and_borough


def get_quietest_city_and_borough(data):
    """ fill in the Nones for the dictionary below using the bar party data """

    quietest_city_and_borough = {'city': None, 'borough': None, 'num_city_calls': None, 'num_borough_calls': None}

    boroughs = set([data[x]['borough'] for x in range(1, len(data))])
    cities = set([data[x]['city'] for x in range(1, len(data))])
    
    borVal = [0] * len(boroughs)
    
    citVal = [0] * len(cities)
    
    for rec in data:
        for idx, val in enumerate(boroughs):
            if rec['borough'] == val:
                borVal[idx] = borVal[idx] + int(rec['num_calls'])
                break
            
    borValSorted = list(zip(boroughs, borVal))
    
    borValSorted.sort(key = sortVal)
    
    #print(borValSorted[0])
            
    for rec in data:
        for idx, val in enumerate(cities):
            if rec['city'] == val:
                citVal[idx] = citVal[idx] + int(rec['num_calls'])
                break
    
    citValSorted = list(zip(cities, citVal))
    
    citValSorted.sort(key = sortVal)
    
    #print(citValSorted[0])
    
    quietest_city_and_borough['city'] = citValSorted[0][0]
    quietest_city_and_borough['borough'] = borValSorted[0][0]
    quietest_city_and_borough['num_city_calls'] = citValSorted[0][1]
    quietest_city_and_borough['num_borough_calls'] = borValSorted[0][1]
    
    return quietest_city_and_borough


if __name__ == '__main__':
    bar_data = get_bar_party_data()

    # uncomment the line below to see what the data looks like
    #print_data(bar_data)
    

    noisy_metrics = get_most_noisy_city_and_borough(bar_data)

    quiet_metrics = get_quietest_city_and_borough(bar_data)

    print('Noisy Metrics: {}'.format(noisy_metrics))
    print('Quiet Metrics: {}'.format(quiet_metrics))
