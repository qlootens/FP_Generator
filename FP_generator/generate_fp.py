"""
Customizable FP-Generator + Calculator

Written by Quinten Lootens 2017
For more information, hit me on github (qlootens)!
"""

def calculate_fp(bits_pwr, bits_mnts, fp):
    if bits_pwr + bits_mnts + 1 != len(fp):
        return "Invalid input"

    # Calculate the BIAS: 2 ** (number of bits in power) - 1
    bias = (2 ** (bits_pwr - 1)) - 1

    # Split the power and the mantisse bits from the fp bits.
    power_bits = fp[1:(bits_pwr+1)]
    mnts_bits = fp[(bits_pwr + 1):]

    pwr = calculate_power(power_bits) - bias
    mnts = calculate_mantisse(mnts_bits)

    # Make a difference between normalized and denormalized numbers.
    normalized = 1.0
    sign_bit = 1.0

    # Calculate the Sign Bit: "1" for the negative numbers, "0" for the positive.
    if fp[0] == "1":
        sign_bit = -1.0

    # Calculate if the power_bits represent a denormalized number.
    if power_bits == "0" * bits_pwr:
        normalized = 0.0

        # Check if the fp_bits represent a Clean Zero
        if mnts == 0:
            return 0.0

    # Check if the fp_bits represent Infinity
    if power_bits == "1" * bits_pwr and mnts_bits == "0" * bits_mnts:
        return "infinity"

    # Check if the fp_bits represent NaN
    if power_bits == "1" * bits_pwr and mnts > 0:
        return "NaN"

    # Calculate the fp_number
    return sign_bit * (mnts + normalized) * (2.0 ** pwr)


def calculate_mantisse(mantisse):
    mnts = 0.0
    pwr = 1
    for bit in mantisse:
        if bit == '1':
            mnts += (1.0 / (2.0 ** pwr))
        pwr += 1
    return mnts


def calculate_power(power):
    exp = 0.0
    pwr = 0.0
    power = power[::-1]
    for bit in power:
        if bit == '1':
            exp += (2 ** pwr)
        pwr += 1
    return exp

