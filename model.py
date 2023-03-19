
class DataSet:
  def __init__(self, creationMonthNumber, age):
    self.creationMonthNumber = creationMonthNumber
    self.age = age
  def __str__(self):
    return f"{self.creationMonthNumber}({self.age})"
  def increment(self):
    self.age += 1

class Store:
  def __init__(self, ageTrigger, previous):
    self.ageTrigger = ageTrigger
    self.previous = previous
    self.dataSet = None

  def __str__(self):
    return f"({self.ageTrigger})"
  def add(self, dataSet):
    self.dataSet = dataSet
  def fill(self):
    if self.previous is not None:
       self.dataSet = self.previous.dataSet
       self.previous.fill()
 
storeCount =7
one = Store(1, None)
two = Store(2, one)	
three = Store(3, two)	
five = Store(5, three)
eight = Store(8, five)
thirteen = Store(13, eight)
twentyOne =	Store(21, thirteen)


stores = {
    "one" : one,
    "two" : two,
    "three" : three,
    "five" : five,
    "eight" : eight,
    "thirteen" : thirteen,
    "twentyOne" : twentyOne
} 
storeNames = ["one",
    "two" ,
    "three" ,
    "five" ,
    "eight" ,
    "thirteen" ,
    "twentyOne" ]

def age():
    for storeName in storeNames: 
        ds = stores[storeName].dataSet
        if ds is not None:
            ds.increment() 
def firstNull():
    for storeName in storeNames: 
        if stores[storeName].dataSet is None:
            return stores[storeName]
    return None

def moveintoEmpty():
    empty = firstNull()
    if empty is None:
        empty = makeEmpty()
    empty.fill()

def makeEmpty():
    for storeName in storeNames: 
        if stores[storeName].dataSet.age < stores[storeName].ageTrigger:
            stores[storeName].dataSet = None
            return stores[storeName]

def addToStores(dataSet):
    moveintoEmpty()
    stores["one"].dataSet = dataSet

for x in range(0, 70):
    age()
    dataSet = DataSet(x,0)
    addToStores(dataSet)

for storeName in storeNames: 
    print(stores[storeName], stores[storeName].dataSet.age)