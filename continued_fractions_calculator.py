#a continued fractions calculator
def cont_frac_calculator(sequence):
    if len(sequence) == 1:
        print(f"list only has element {sequence[0]}")
        return sequence[0]

    print(f"list is currently {sequence}")
    first_term = sequence.pop(0)
    return first_term + 1/(cont_frac_calculator(sequence))
"""
sequence = [1,1,1,1,1,1,1,1]
cont_fraction = cont_frac_calculator(sequence)
print(cont_fraction)
"""