cars = {'make': 'bmw',
        'model': '2022',
        'color': 'black'}
car_model = cars['model']
print(car_model)

# nested dictionary

cars2 = {'make': 'bmw',
        'model': '2022',
        'color': 'black',
         'area':{
                 'country':'Bangladesh',
                 'city':'Dhaka',
                 'road':{
                         'new_road_number':'12/1',
                         'old_road_number':'10'
                 }
         }}

print(cars2['area']['city'])
print(cars2['area']['road']['new_road_number'])

print(cars2.keys())
print(cars2.values())