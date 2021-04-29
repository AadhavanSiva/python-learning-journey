# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 19:27:26 2021

@author: Aadhavan
"""

import tkinter as tk
import requests




def getCountrycurrencies():
    country_curriency = country_curriency_var.get()
    print(country_curriency)

    response = requests.get('https://restcountries.eu/rest/v2/currency/' + country_curriency)

    # print response

    # print json content
    # print(response.json())
    country_details = response.json()
    for currency in country_details:
        print(f"Name = {currency['name']}, Code = {currency['alpha2Code']}  region = {currency['region']} subregion = {currency['subregion']}")
        for curr in currency['currencies']:

            print( f"Symbol = {curr['symbol']}, Name = {curr['name']}")






















# API - Application Program Interface
# JSON - formatted data
# requests module - To get data from internet (requests.get("url") ) and return response object
# json object - response.json()
# some apis will give the response as list, whereas some will give only one object.
# https://restcountries.eu/rest/v2/name/India
# https://restcountries.eu/rest/v2/alpha/IN

# Now Try to print area and timezones
# homework
# https://restcountries.eu/rest/v2/currency/inr - print currency details for name, symbol, sub region and region

def getCountryCodes():

    country_name = country_name_var.get()
    print(country_name)
    
    response = requests.get("https://restcountries.eu/rest/v2/name/" + country_name)

    # print response
    print(response)

    # print json content
    # print(response.text)
    country_details = response.json()
    print(country_details)
    #print(response.status_code)

    for country in country_details:
        print(f"Name = {country['name']}, Code = {country['alpha3Code']}  region = {country['region']}")


def getCountryDetail():
    country_code = country_code_var.get()
    print(country_code)

    response = requests.get('https://restcountries.eu/rest/v2/alpha/' + country_code)

    # print response
    print(response)

    # print json content
    # print(response.json())
    country_detail = response.json()
    print(country_detail)

    print(f"Name = {country_detail['name']}, Capital = {country_detail['capital']}")
    print(f"population = {country_detail['population']}, region = {country_detail['region']}")
    print(f"subregion = {country_detail['subregion']}")
    print(f"timezone = {country_detail['timezones']}")
    print(f"area = {country_detail['area']}")
    print( "Borders are :")
    print( country_detail['borders'] )




main = tk.Tk()
main.geometry("500x200")
country_code_var = tk.StringVar()
country_name_var = tk.StringVar()
country_curriency_var = tk.StringVar()

tk.Label(main, text='Country Code').grid(row=2)

CountryCodeEntry = tk.Entry(main,textvariable=country_code_var).grid(row=2, column=1)


tk.Label(main, text='Country Name').grid(row=4)
CountryNameEntry = tk.Entry(main,textvariable=country_name_var).grid(row=4, column=1)
tk.Label(main, text='Country curriency').grid(row=5)
countrycurriencyEntry = tk.Entry(main,textvariable=country_curriency_var).grid(row=5, column=1)




btn = tk.Button(main, text="Get Country code(s)", command=getCountryCodes).grid(row=7, column=1)
btn = tk.Button(main, text="Get Country Details", command=getCountryDetail).grid(row=7, column=2)
btn = tk.Button(main, text="Get Country currencies", command=getCountrycurrencies).grid(row=7, column=3)


main.mainloop()