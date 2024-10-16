import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myVar = pd.DataFrame(mydataset)

print(myVar)

print(pd.__version__)