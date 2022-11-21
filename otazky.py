def otazka1(data):
    otazka = data.columns[-1]
    ano = 0
    nie = 0
    for riadok in data.iterrows():
        if(riadok[1][-1]=="Áno"):
            ano += 1
        else:
            nie += 1
    print(str(otazka)+"\n"+"Áno: "+str(ano)+"\nNie: "+str(nie))
def otazka2(data):
    otazka = data.columns[-1]
    ano = 0
    nie = 0
    for riadok in data.iterrows():
        if(riadok[1][-1]=="Áno"):
            ano += 1
        else:
            nie += 1
    print(str(otazka)+"\n"+"Áno: "+str(ano)+"\nNie: "+str(nie))
    return 0
def otazka3(data):
    otazka = data.columns[-1]
    ano = 0
    nie = 0
    for riadok in data.iterrows():
        if(riadok[1][-1]=="Áno"):
            ano += 1
        else:
            nie += 1
    print(str(otazka)+"\n"+"Áno: "+str(ano)+"\nNie: "+str(nie))
    return 0
def otazka4(data):
    otazka = data.columns[-1]
    vlajka = 0
    kronika = 0
    fotoalbum = 0
    erb = 0
    ritual = 0
    nastenka = 0
    for riadok in data.iterrows():
        if("Vlajka" in riadok[1][-1]):
            vlajka += 1
        if ("Kronika" in riadok[1][-1]):
            kronika += 1
        if ("Fotoalbum/Online galéria fotiek" in riadok[1][-1]):
            fotoalbum += 1
        if ("Erb/kus oblečenia/iná insígnia" in riadok[1][-1]):
            erb += 1
        if ("Špecifický rituál/Tradícia/Pokrik" in riadok[1][-1]):
            ritual += 1
        if ("Nástenka" in riadok[1][-1]):
            nastenka += 1
    print(str(otazka)+"\n"+"Vlajka: "+str(vlajka)+"\nKronika: "+str(kronika)+"\nFotoalbum: "+str(fotoalbum)+"\nErb: "+str(erb)+"\nRituál: "+str(ritual)+"\nNástenka: "+str(nastenka))
    return 0