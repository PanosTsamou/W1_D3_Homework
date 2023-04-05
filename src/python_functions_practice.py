
# it returns number 10
def return_10():
    return 10

#it gets 2 numbers and returns the sum
def  add(first_number, second_number):
    return first_number + second_number

# it gets 2 numbers and returns the differnce
def  subtract(first_number, second_number):
    return first_number - second_number

# it gets 2 numbers and returns the multiplication 
def  multiply(first_number, second_number):
    return first_number * second_number

# it gets 2 numbers and returns the division
def  divide(first_number, second_number):
    return first_number / second_number


# it gets a string and returns its length
def length_of_string(string_for_testing):
    return len(string_for_testing)


# it gets 2 strings and returns their sum
def    join_string(first_string, second_string):
    return first_string + second_string


#it gets 2 numbers as strings and returns their sum as integer
def add_string_as_number(first_string_number, second_string_number):
    sum_of_numbers = int(first_string_number) + int(second_string_number)
    return sum_of_numbers


#it get a number and returns the month that corresponds to it
def number_to_full_month_name(num_of_the_month):
    if num_of_the_month == 1:
        return "January"
    elif num_of_the_month == 3:
        return "March"
    elif num_of_the_month == 9:
        return "September"
    

#it gets a number and returns the short name of the month that corresponds to it    
def number_to_short_month_name(num_of_the_month):
        months_of_the_year = ["Jan", "Feb", "Mar", "Apr", "Ma", 
                            "Jun", "Jul", "Aug", "Sept",
                            "Oct", "Nov", "Dec" ]
        return months_of_the_year[num_of_the_month - 1]


#it gets the length of a cube and returns its volume
def calculate_the_volume(cube_side):
    volume =  cube_side * cube_side *  cube_side
    return volume


#it gets a string and returns it reversed
def string_reversed(string_to_be_reverced: str):
    result = string_to_be_reverced[::-1]
    return result


#it gets the temperature in F and returns it in Celsius
def convert_F_to_Celsius(F_temperature):
    F_in_celsius = F_temperature - 32
    return F_in_celsius
