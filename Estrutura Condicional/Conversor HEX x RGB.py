red = int(input('\033[31mRED\033[m: '))
green = int(input('\033[32mGREEN\033[m: '))
blue = int(input('\033[34mBLUE\033[m: '))
if red <= 255 and blue <= 255 and green <= 255:
    print(f'Valor em HEX: #{red:02X}{green:02X}{blue:02X} ')
else:
    print('n tem n')
