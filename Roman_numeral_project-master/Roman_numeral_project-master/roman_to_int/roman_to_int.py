class roman_tools:
    def roman_to_int(self,r):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        r=str(r)
        for i in range(len(r)):
            if i > 0 and rom_val[r[i]] > rom_val[r[i - 1]]:
                int_val += rom_val[r[i]] - 2 * rom_val[r[i - 1]]
            else:
                int_val += rom_val[r[i]]
        return int_val

    def square_roman(r):
        return int_val^2