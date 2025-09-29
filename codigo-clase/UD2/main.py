import pandas as pd

data = {
    "Nombre": ["Ana", "Luis", "Juan"],
    "Edad": [23, 21, 22],
    "Ciudad": ["Madrid", "Barcelona", "Sevilla"],
}

df = pd.DataFrame(data)
print(df)

print('-------')

# Mostrar personas entre 23 y 30 años
print(df[(df["Edad"] >= 23) & (df["Edad"] <= 30)])

# 