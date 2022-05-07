class roman_tools:
    def roman_to_int(self,r):
        #dictionary containing roman numerals
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        #start the int_val at 0
        int_val = 0
        #for loop to iterate through roman numeral
        for i in range(len(r)):
            #if statement to decide if vales are bigger than each other
            if i > 0 and rom_val[r[i]] > rom_val[r[i - 1]]:
                int_val += rom_val[r[i]] - 2 * rom_val[r[i - 1]]
            else:
                int_val += rom_val[r[i]]
        return int_val