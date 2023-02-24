def latinName(name):
    result = False

    last_pos = len(name) - 1
    if name[last_pos].lower() != "y":
        result = "{}y".format(name)
    else:
        result = "{}iful".format(name[0:last_pos])
    return result


print(latinName("sparky"))
print(latinName("spot"))
