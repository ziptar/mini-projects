led_digit_zero = ("███", "█ █", "█ █", "█ █", "███")
led_digit_one = ("  █", "  █", "  █", "  █", "  █")
led_digit_two = ("███", "  █", "███", "█  ", "███")
led_digit_three = ("███", "  █", "███", "  █", "███")
led_digit_four = ("█ █", "█ █", "███", "  █", "  █")
led_digit_five = ("███", "█  ", "███", "  █", "███")
led_digit_six = ("███", "█  ", "███", "█ █", "███")
led_digit_seven = ("███", "  █", "  █", "  █", "  █")
led_digit_eight = ("███", "█ █", "███", "█ █", "███")
led_digit_nine = ("███", "█ █", "███", "  █", "███")

led_digits_tuple = (
    led_digit_zero, 
    led_digit_one,
    led_digit_two,
    led_digit_three,
    led_digit_four,
    led_digit_five,
    led_digit_six,
    led_digit_seven,
    led_digit_eight,
    led_digit_nine
    )

def make_rows_list(dig_list):
    rows_list = []
    for row in range(5):        
        cols = []
        for dig in dig_list:
            cols.append(dig[row])
        rows_list.append(" ".join(cols))
        
    return rows_list

def display(dig_list):
    rows_list = make_rows_list(dig_list)
    for row in range(5):
        print(rows_list[row])
 
def make_led_digits_list(dig_str):
    led_digits_list = []
    for ds in dig_str:
        led_digits_list.append(led_digits_tuple[int(ds)])
        
    return led_digits_list             


digits_str = input("Enter a positive integer: ")
if digits_str.isdigit():
    led_digits_list = make_led_digits_list(digits_str)
    display(led_digits_list)
else:
    print("Error: The value you entered is not valid.")      
