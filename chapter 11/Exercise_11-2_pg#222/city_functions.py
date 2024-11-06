def place(city,country,population):
    txt = city + ', ' + country + ' - population ' + str(population)
    return txt.title()

if __name__ == "__main__":
    print(place('karachi','pakistan',22000000))