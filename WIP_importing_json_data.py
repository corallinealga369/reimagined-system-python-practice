#! python3

import json

filename = 'shipsuicideratemd'
with open(filename) as f:
    pop_data=json.load(f)

#print the 2014-2016 suicide rate data for each city
for pop_dict in pop_data:
    if pop_dict['Year']=='2014-2016':
        jurisdiction=pop_dict['jurisdiction']
        race_ethnicity=pop_dict['race_ethnicity']
        year=pop_dict['year']
        measure=pop_dict['measure']
        print(jurisdiction+' : '+measure)
