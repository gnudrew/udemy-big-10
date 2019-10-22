def uncompress_temps(temperatures):        
    new_temps = [
        temp / 10 
        for temp in temperatures
        ]
    return new_temps

# Data stored by omitting the decimel. Divide by 10 to get it back.
temps = [120, 132, 153, 214]

print(temps)
print(uncompress_temps(temps))