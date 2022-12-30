#count_divisions returns the integer part of log_base(number)
def nearest_power(number,base,count):
    if number < base:
        print(f"{number} is less than {base}. No more divisions are possible. Total number of divisions is {count}")
        return number, base, count
    else:
        count += 1
        new_number = number/base
        print(f"{number} is greater than {base}. After division, new number is {new_number} and total no. of divisions is {count}")
        return nearest_power(new_number,base,count)
"""
numerator = input("This Python script will find the quotient of a pair of numbers. What is the numerator? ")
denominator = input("Thank you. What is the denominator? ")
numerator, denominator = float(numerator), float(denominator)
power = nearest_power(numerator, denominator, 0)
remainder = numerator - denominator**power
print(f"{int(numerator)} equals {int(denominator)}^{int(power)} + {int(remainder)}.")
"""