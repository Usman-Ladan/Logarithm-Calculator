#logarithm calculator. The tolerance is how many terms in the continued fraction we use
from count_divisions import nearest_power
from continued_fractions_calculator import cont_frac_calculator
def calculate_sequence(number, base, tolerance, sequence):
    if number <= 0:
        print("This file cannot calculate logs of negative numbers. Pease input a valid value")
    if base == 1:
        print("The base cannot equal 1. Please input a valid value")
        return
    
    if base <= 0:
        print("This file cannot calculate logs for negative bases. Please input a valid value")
        return
    
    if 0 < base < 1:
        new_base = base**-1
        print(f"{base} is between 0 and 1. {base}^-1 ~= {new_base:.2f} to 2 sig figs. So, we calculate the sequence for log_({new_base})({number})")
        return calculate_sequence(number, new_base, tolerance, sequence)
    
    if len(sequence) == tolerance:
        print(f"we have {tolerance} terms in our sequence")
        return sequence

    new_base, old_base, next_term = nearest_power(number, base, 0)
    sequence.append(next_term)
    #if new_base is 1, number was a power of the base so return the sequence. Else, call calculate_sequence again.
    if new_base == 1:
        print("We have reached either perfect division or a rounding error before reaching the tolerance.")
        print(f"We have {len(sequence)} term in our sequence")
        return sequence
    return calculate_sequence(old_base, new_base, tolerance, sequence)

def calculate_log(number, base, tolerance):
    print(f"Calculating log_{base}({number}) up to a sequence tolerance of {tolerance}")
    terms = calculate_sequence(number, base, tolerance, [])
    log = cont_frac_calculator(terms)
    #series of contitions based on if number and/or base is between 0 and 1
    if 0 < base < 1:
        log = -log
    if 0 < number < 1:
        log = -log
    print(f"We have that log_{base}({number}) ~= {log} up to sequence tolerance {tolerance}")
    estimate = base**log
    print(f"From our calculation of log, we get an estimate for the original number as {estimate}.\nThe original number was {number}.")

number = input("This Python script calculates the log of two numbers. What number do you want to calculate the log of? ")
base = input("Ok then. What base do you want to use? ")
tolerance = input("Wonderful. Finally, what sequence tolerance do you desire? ")
number = float(number)
base = float(base)
tolerance = int(tolerance)
calculate_log(number, base, tolerance)
