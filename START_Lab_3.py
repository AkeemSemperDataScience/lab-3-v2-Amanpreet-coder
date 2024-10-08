
def lab3Question1(number, cutoff):
    # Take in two arguments - a number and a 'cutoff' (another number)
    # Return True if the number is less than the cutoff, False otherwise
    # Also, print a statement of "[Number] is less than [cutoff]" or "[Number] is not less than [cutoff]"
    # Where the [Number] and [cutoff] are the actual numbers passed in
    if(number < cutoff):
        print(f'{number} is less than {cutoff}')
        return True
    else:
        print(f'{number} is not less than {cutoff}')
        return False

def lab3Question2(decimal_number):
    # Take in an argument of a float (decimal) number.
    # Return "zero" if the number is 0, "positive" if the number is positive, and "negative" if the number is negative
    # Return "invalid" if the input is not a float
    if not isinstance(decimal_number, (float,int)):
        return "invalid"
    if decimal_number == 0:
        return "zero"
    elif decimal_number > 0:
        return "positive"
    else:
        return "negative"

def lab3Question3(year):
    # Take in a number that represents a year
    # Return "21st century" if the year is between 2001 and 2100,
    # "20th century" if the year is between 1901 and 2000,
    # "19th century" if the year is between 1801 and 1900, 
    # "ancient" if the year is older
    # "invalid" if the input is not an acceptable year number. 
    if not isinstance(year, int) or year <= 0:
        return "invalid"
    if year >= 2001 and year <= 2100:
        return "21st century"
    elif year >= 1901 and year <= 2000:
        return "20th century"
    elif year >= 1801 and year <= 1900:
        return "19th century"
    elif year <= 1800:
        return "ancient"
    else:
        return "invalid"

def lab3Question4(number_1, number_2, number_3):
    # Take in three numbers as arguments
    # Return the largest of the three numbers
    # Return None if the inputs are not 3 numbers
    if not isinstance(number_1, (int, float)) or not isinstance(number_2, (int, float)) or not isinstance(number_3, (int, float)):
        return None
    if number_1 >= number_2 and number_1 >= number_3:
        return number_1
    elif number_2 >= number_1 and number_2 >= number_3:
        return number_2
    else:
        return number_3

def lab3Question5(temperature, scale_used):
    # Take in a temperature and the scale that the temperature is in - either "C" for Celsius or "F" for Fahrenheit (capitalized)
    # Return "Liquid" if water is in liquid state at that temperature
    # Return "Solid" if water is in solid state at that temperature
    # Return "Gas" if water is in gas state at that temperature
    # Return "Invalid" if the temperature or scale are invalid
    if not isinstance(temperature, (int, float)) or scale_used not in ["C", "F"]:
        return "Invalid"
    if scale_used == "C":
        if temperature <= 0:
            return "Solid"
        elif temperature > 0 and temperature < 100:
            return "Liquid"
        else:
            return "Gas"
    elif scale_used == "F":
        if temperature <= 32:
            return "Solid"
        elif temperature > 32 and temperature < 212:
            return "Liquid"
        else:
            return "Gas"

