import pandas as pd

series = pd.Series(['Semarang', 'Pati', 'Sintang', 'Sanggau', 'Sambas'])

series1 = pd.Series(['Semarang', 'Pati', 'Sintang', 'Sanggau', 'Sambas'],
                    index=['A', 'B', 'C', 'D', 'E'])

print(series)

print('')

print(series1)
