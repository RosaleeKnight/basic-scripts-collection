def format_address(address_string):
    building_number = ''
    street_name = ''
    address_string = address_string.split()

    for string in address_string:
        if string.isdigit():
            building_number = string
        else:
            street_name += string + ' '
    return "building number {} on street named {}".format(building_number, street_name)

print(format_address("123 Main Street"))
print(format_address("426 Portage Ave"))
print(format_address("1 Navy Way"))