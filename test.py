import ephem

mars = ephem.Jupiter("2000/01/01")
const = ephem.constellation(mars)
print(const)