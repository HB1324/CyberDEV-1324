def calculate_h10301(facility_code, card_number):
    if not (0 <= facility_code <= 255):
        raise ValueError("Facility code must be between 0 and 255")
    if not (0 <= card_number <= 65535):
        raise ValueError("Card number must be between 0 and 65535")

    # Convert facility code and card number to binary
    fc_bin = f"{facility_code:08b}"
    cn_bin = f"{card_number:016b}"

    # Combine facility code and card number to form the 24-bit data (without parity)
    card_data = fc_bin + cn_bin

    # Calculate the parity for the first 13 bits (even parity)
    first_half = card_data[:13]
    first_parity = "0" if first_half.count('1') % 2 == 0 else "1"

    # Calculate the parity for the last 13 bits (odd parity)
    second_half = card_data[13:]
    second_parity = "1" if second_half.count('1') % 2 == 0 else "0"

    # Create the full 26-bit binary representation
    full_binary = first_parity + card_data + second_parity

    # Convert the binary representation to hexadecimal
    full_hex = f"{int(full_binary, 2):06X}"

    return {
        "facility_code": facility_code,
        "card_number": card_number,
        "binary": full_binary,
        "hexadecimal": full_hex,
    }

# Example Usage
facility_code = int(input("Enter Facility Code: "))  # Example facility code
card_number = int(input("Enter 5-Digit Card #: "))  # Example card number
card_data = calculate_h10301(facility_code, card_number)

print(f"Facility Code: {card_data['facility_code']}")
print(f"Card Number: {card_data['card_number']}")
print(f"Binary Representation: {card_data['binary']}")
print(f"Hexadecimal Representation: {card_data['hexadecimal']}")
