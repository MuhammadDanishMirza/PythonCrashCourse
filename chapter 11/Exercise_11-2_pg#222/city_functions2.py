def place(city,country,population=''):
    if population:
        txt = city + ', ' + country + ' - population ' + str(population)
    else:
        txt = city + ', ' + country
    return txt.title()

if __name__ == "__main__":
    print(place('karachi','pakistan',22000000))