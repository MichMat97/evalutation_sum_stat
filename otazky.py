import math
import numpy as np
import statistics as stat

otazka1_data = {"Áno": 0, "Nie": 0}
otazka1_data_zbory = {}
otazka1_data_oblasti = {}
otazka2_data = {"Áno": 0, "Nie": 0}
otazka3_data = {"Áno": 0, "Nie": 0}
otazka4_data = {"Vlajka": 0, "Kronika": 0, "Fotoalbum/Online galéria fotiek": 0,
                "Erb/kus oblečenia/iná insígnia": 0, "Špecifický rituál/Tradícia/Pokrik": 0,
                "Nástenka": 0}
otazka5_data = {"Vĺčatá/včielky": 0, "Skauti/skautky": 0, "Rangeri/rangerky": 0, "Roveri/roverky": 0,
                "Dospelí skauti a skautky": 0, "Predškoláci": 0, "Žena": 0, "Muž": 0}

otazka5_data_2 = {"Vĺčatá/včielky": [], "Skauti/skautky": [], "Rangeri/rangerky": [], "Roveri/roverky": [],
                  "Dospelí skauti a skautky": [], "Predškoláci": [], "Žena": [], "Muž": []}


def otazka1(data):
    otazka1_data[data[-1]] += 1
    if data[-1] == "Nie":
        if data["Nadriadená jednotka 1"] not in otazka1_data_zbory.keys():
            otazka1_data_zbory[data["Nadriadená jednotka 1"]] = 1
        else:
            otazka1_data_zbory[data["Nadriadená jednotka 1"]] += 1
        if data["Nadriadená jednotka 2"] not in otazka1_data_oblasti.keys():
            otazka1_data_oblasti[data["Nadriadená jednotka 2"]] = 1
        else:
            otazka1_data_oblasti[data["Nadriadená jednotka 2"]] += 1
    return otazka1_data

def otazka1_raw_data():
    return otazka1_data
def otazka1_print_data():
    return "\n" + "Áno: " + str(otazka1_data["Áno"]) + "\nNie: " + str(otazka1_data["Nie"])
def otazka1_print_data_zbory():
    to_print = ""
    for i in otazka1_data_zbory.keys():
        to_print += "\n" + i + " - Nie: " + str(otazka1_data_zbory[i])
    return to_print
def otazka1_print_data_oblasti():
    to_print = ""
    for i in otazka1_data_oblasti.keys():
        to_print += "\n" + i + " - Nie: " + str(otazka1_data_oblasti[i])
    return to_print
def otazka2(data):
    otazka2_data[data[-1]] += 1
    return otazka2_data


def otazka2_print_data():
    return "\n" + "Áno: " + str(otazka2_data["Áno"]) + "\nNie: " + str(otazka2_data["Nie"])


def otazka3(data):
    otazka3_data[data[-1]] += 1
    return otazka3_data


def otazka3_print_data():
    return "\n" + "Áno: " + str(otazka3_data["Áno"]) + "\nNie: " + str(otazka3_data["Nie"])


def otazka4(data):
    for odpoved in otazka4_data.keys():
        if (odpoved in data[-1]):
            otazka4_data[odpoved] += 1
    return otazka4_data


def otazka4_print_data():
    return "\n" + "Vlajka: " + str(otazka4_data["Vlajka"]) + "\nKronika: " + str(
        otazka4_data["Kronika"]) + "\nFotoalbum: " + str(
        otazka4_data["Fotoalbum/Online galéria fotiek"]) + "\nErb: " + str(
        otazka4_data["Erb/kus oblečenia/iná insígnia"]) + "\nRituál: " + str(
        otazka4_data["Špecifický rituál/Tradícia/Pokrik"]) + "\nNástenka: " + str(otazka4_data["Nástenka"])


def otazka5(data):
    odpoved = str.split(data[-1], "\n")
    for i in range(0, len(odpoved) - 1):
        riadok = str.split(odpoved[i], ": ")
        otazka5_data[riadok[0]] += int(riadok[1])
    pohlavia = str.split(odpoved[-1], "Muž: ")
    otazka5_data["Muž"] += int(str.split(pohlavia[1], ")")[0])
    zeny = str.split(pohlavia[0], ": ")
    otazka5_data["Žena"] += int(zeny[1])
    return otazka5_data


def otazka5_print_data():
    print = ""
    for i in otazka5_data.keys():
        print += "\n" + i + ": " + str(otazka5_data[i])
    return print


def otazka5_2(data):
    odpoved = str.split(data[-1], "\n")
    for i in range(0, len(odpoved) - 1):
        riadok = str.split(odpoved[i], ": ")
        otazka5_data_2[riadok[0]].append(int(riadok[1]))
    pohlavia = str.split(odpoved[-1], "Muž: ")
    otazka5_data_2["Muž"].append(int(str.split(pohlavia[1], ")")[0]))
    zeny = str.split(pohlavia[0], ": ")
    otazka5_data_2["Žena"].append(int(zeny[1]))
    return otazka5_data_2


def otazka5_print_data_2():
    to_print = ""
    for i in otazka5_data.keys():
        to_print += "\n" + i + ": " + str(sum(otazka5_data_2[i])) + "\tmin: " + str(min(otazka5_data_2[i])) \
                    + "\tmax: " + str(max(otazka5_data_2[i])) + "\tmodus: " \
                    + str(max(set(otazka5_data_2[i]), key=otazka5_data_2[i].count)) \
                    + "\tmedian: " + str(stat.median(otazka5_data_2[i])) + "\tar. priemer: " \
                    + str(stat.mean(otazka5_data_2[i]))
    return to_print

def otazka5_print_data_2_raw():
    data = {}
    for i in otazka5_data.keys():
        data[i] = [sum(otazka5_data_2[i]), min(otazka5_data_2[i]), max(otazka5_data_2[i]),
                   max(set(otazka5_data_2[i]), key=otazka5_data_2[i].count), stat.median(otazka5_data_2[i]),
                   stat.mean(otazka5_data_2[i])]
    return data

def otazka5_print_data_2_category():
    return ['Súčet', 'Minimum', 'Maximum', 'Modus', 'Medián', 'Aritmetický priemer']