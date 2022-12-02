import numpy as np
import pandas as pd

import latex
import otazky
from datetime import datetime, date

export_file_name = 'all2020.xlsx'
dset = pd.ExcelFile(export_file_name)
df = dset.parse('Odpovede')
df.columns = df.columns.str.strip()
df.head()

obal = ["Jednotka", "Nadriadená jednotka 1", "Nadriadená jednotka 2", "Typ oddielu", "Stav hodnotenia"]

znenie_otazok = ["Máte od všetkých vašich členov prihlášky?",
                 "Má každý váš člen preukaz s platnou registračnou známkou?",
                 "Má každý člen starší ako 16 rokov aktívny účet v Teepee?",
                 "Ktoré z nasledujúcich má váš oddiel?",
                 "Koľko registrovaných členov mal váš oddiel?"]

for riadok in df.iterrows():
    otazky.otazka1(riadok[1].loc[obal+[znenie_otazok[0]]])
    otazky.otazka2(riadok[1].loc[obal+[znenie_otazok[1]]])
    # otazky.otazka3(riadok[1].loc[obal+[znenie_otazok[2]]])
    # otazky.otazka4(riadok[1].loc[obal+[znenie_otazok[3]]])
    otazky.otazka5(riadok[1].loc[obal + [znenie_otazok[4]]])

# print(str(znenie_otazok[0])+otazky.otazka1_print_data())
# print(str(znenie_otazok[0])+otazky.otazka1_print_data_zbory())
# print(str(znenie_otazok[0])+otazky.otazka1_print_data_oblasti())

# print(str(znenie_otazok[1])+otazky.otazka2_print_data())
# print(str(znenie_otazok[2])+otazky.otazka3_print_data())
# print(str(znenie_otazok[3])+otazky.otazka4_print_data())
#print(str(znenie_otazok[4])+otazky.otazka5_print_data_2())


latex.oneLineQuestion(znenie_otazok[0], otazky.otazka1_raw_data())
latex.multiLineQuestion(znenie_otazok[1], otazky.otazka2_print_data_raw())
latex.multiLineQuestion(znenie_otazok[4], otazky.otazka5_print_data_raw())

np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
#print(otazky.otazka5_print_data_2_raw().iloc[0])
#print(otazky.otazka5_print_data_2_raw().index.values[0])
#print(otazky.otazka5_print_data_raw().iloc[0][0])
# for rowIndex in range(1, len(otazky.otazka5_print_data_2_raw().values)):
#     #print(otazky.otazka5_print_data_2_raw().index.values[rowIndex])
#     print(type(otazky.otazka5_print_data_2_raw().iloc[rowIndex]))

latex.savePDF()
