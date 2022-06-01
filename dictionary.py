def dictionary():
  car={
  "brand" : "bmw",
  "model" : "xj" ,
  "year" : 2014
}
  print (car.get("year"))
  print(car.get("brand"))
  car1=car.copy() #copy Dictionary value
  print (car1)
  car1.update({"type" : "hybrid"}) # Add new Key value pair
  print(car1)
  del car1['year']   # delete Key value pair
  print(car1)
dictionary()