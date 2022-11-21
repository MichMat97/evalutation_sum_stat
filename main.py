import pandas as pd
import otazky as o
from datetime import datetime, date


export_file_name = 'export.xlsx'
dset = pd.ExcelFile(export_file_name)
df = dset.parse('Odpovede')
df.columns = df.columns.str.strip()
df.head()

obal = ["Jednotka", "Nadriadená jednotka 1", "Nadriadená jednotka 2", "Typ oddielu", "Stav hodnotenia"]

znenie_otazok = ["Máte od všetkých vašich členov prihlášky?",
                 "Má každý váš člen preukaz s platnou registračnou známkou?",
                 "Má každý člen starší ako 16 rokov aktívny účet v Teepee?",
                 "Ktoré z nasledujúcich má váš oddiel?"]

#o.otazka1(df[["Jednotka", "Nadriadená jednotka 1", "Nadriadená jednotka 2", "Typ oddielu", "Stav hodnotenia", znenie_otazok[0]]])
#o.otazka2(df[["Jednotka", "Nadriadená jednotka 1", "Nadriadená jednotka 2", "Typ oddielu", "Stav hodnotenia", znenie_otazok[1]]])
#o.otazka3(df[["Jednotka", "Nadriadená jednotka 1", "Nadriadená jednotka 2", "Typ oddielu", "Stav hodnotenia", znenie_otazok[2]]])
#o.otazka4(df[["Jednotka", "Nadriadená jednotka 1", "Nadriadená jednotka 2", "Typ oddielu", "Stav hodnotenia", znenie_otazok[3]]])

for riadok in df.iterrows():
    print(riadok[1].loc[obal+[znenie_otazok[2]]])
