
def avg(*args):
    avg = sum(args) / len(args)
    print(avg)

while True:
    number = int(input("Enter a number: "))

    match number:

        case "Calculate":
            avg(number)

        case number.isdigit():
            pass


