#NYOMAN ADI ARYA SUABAKTI/2415091013
n = int(input())

if 1 <= n <= 3999:
    output = ""
    units = [
        ("M", 1000),
        ("ZM", 900),
        ("D", 500),
        ("ZD", 400),
        ("Z", 100),
        ("XZ", 90),
        ("L", 50),
        ("XL", 40),
        ("X", 10),
        ("AX", 9),
        ("V", 5),
        ("AV", 4),
        ("A", 1)
    ]
    for symbol, value in units:
        while n >= value:
            output += symbol
            n -= value
    print(output)
else:
    print("No Proceed")