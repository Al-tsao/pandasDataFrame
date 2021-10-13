import pandas as pd

data = pd.DataFrame({"power_level": [12000, 16000, 4000, 1500, 3000, 
                                     2000, 1600, 2000, 300],
                     "uniform color": ["orange", "blue", "black", "orange",
                                       "purple", "green", "orange", "orange","orange"],
                     "species": ["saiyan","saiyan","saiyan","half saiyan",
                                 "namak","human","human","human","human"]}, 
                     index = ["Goku","Vegeta", "Nappa","Gohan",
                                   "Piccolo","Tien","Yamcha", "Krillin","Roshi"])

def my_function(x, h, l):
    if x >  h:
        return("high")
    if x >  l:
        return("med")
    return ("low")
    
data["power_level"].apply(my_function, args = [10000, 2000])