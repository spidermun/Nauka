try:
    nums = []
    with open("liczby.txt","r")as file:
        file = file.readlines()
        for line in file:
            try:
                line_int = int(line)
                nums.append(line_int)
            except ValueError:
                pass
finally:
    parzyste =[print(num ** 2) for num in nums if num % 2 == 0]