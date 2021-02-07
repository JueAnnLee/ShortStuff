# Roman numeral/Decimal converter


# Roman to decimal conversion table
RomanValue = { 'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000 }

def RomanValueList (RomanNumber):
    number = []
    for i in RomanNumber:
        number.append(RomanValue[i])
    return number

# Convert Roman number string to list of decimal conversion values
def ToDecimal (number): # Expects a list from RomanValueList()
    answer = number[-1] # Start with the rightmost digit
    for i in range(len(number)-1,0,-1): # Digits offered in reverse
        right = i
        left = i-1
        if left < 0: # Don't overrun the beginning of the list
            break    # This should never happen anyway.
        else:
            # Process every pair of roman digits with a simple rule.
            if number[left] < number[right]:
                answer -= number[left]
            else:
                answer += number[left]
    return answer

# Decimal to Roman conversion table
ones = { 0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX' }
tens = { 0: '', 1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC' }
huns = { 0: '', 1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM' }
thous = { 0: '', 1: 'M', 2: 'MM', 3: 'MMM' }

# Convert decimal int to Roman number string
def ToRoman (x): # Expects an int 1 to 3999
    one = x//1 % 10 # separate the place values
    ten = x//10 % 10
    hun = x//100 % 10
    thou = x//1000 % 10
    return thous[thou] + huns[hun] + tens[ten] + ones[one]


# Main code starts here
    # accepts improper Roman numbers such as IVMX.
    # may give unexpected conversions for improper Roman numbers.
    # IVMX converts to 1004.  1004 should be MIV in modern standard notation.
    # Does not accept 0, or over large or fractional decimal numbers.
stop = False
while not stop:
    baddata = False
    while not baddata:
        number = ''
        while number == '':
            number = input ("Enter number to convert: ")
        number = number.upper()
        # Anything other than decimal digits, decimal point, or Roman digits is rejected.
        decimal = Roman = True
        for i in number:
            if i not in {'0','1','2','3','4','5','6','7','8','9'}:
                decimal = False
            if i not in {'I','V','X','L','C','D','M'}: # 2 Sets of acceptable chars.
                Roman = False
        if not decimal and not Roman: # Neither type entered.
            if number == 'Q': 
                stop = True # Trying to end the prog here.
                break # Breaks baddata loop.
            else:
                print ("Decimal (1 to 3999) or Roman numbers only, please.")
                continue # Get another input.  Continues baddata loop.
        else: # Process the number input
            if decimal:
                if (int(number) < 1) or (int(number) > 3999):
                    print ("Decimal (1 to 3999) or Roman numbers only, please.")
                    continue
                answer = ToRoman(int(number))
            elif Roman:
                answer = ToDecimal(RomanValueList (number))
        print (number, " converts to ", answer)
# Main code stops here












