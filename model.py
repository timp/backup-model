
class DataSet:
  def __init__(self, creationMonthNumber, age):
    self.creationMonthNumber = creationMonthNumber
    self.age = age
    self.expiry = self.calculateExpiry( creationMonthNumber)
  def __str__(self):
    return f"creation:{self.creationMonthNumber}, age:{self.age}, expiry:{self.expiry}"
  def increment(self):
    self.age += 1
  def calculateExpiry(self, creationMonthNumber): 
    if creationMonthNumber % 32  == 0 :
        return 32
    elif creationMonthNumber % 16  == 0 :
        return 16
    elif creationMonthNumber % 8  == 0 :
        return 8
    elif creationMonthNumber % 4  == 0 :
        return 4
    else :
      return 2
    

dataSets = [] 
def age():
    for ds in dataSets: 
        ds.increment()
    for ds in dataSets: 
        if ds.age > ds.expiry:
            dataSets.remove(ds)
    
        
for x in range(1, 256):
    dataSet = DataSet(x,0)
    dataSets.append(dataSet)
    age()

for ds in dataSets: 
    print(ds)