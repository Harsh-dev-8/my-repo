def analyze_list(numbers):
    
    total = 0
    highest = numbers[0]
    lowest = numbers[0]


    for num in numbers:
        total += num
    
    for num in numbers:
        if num > highest:
            highest = num

    for num in numbers:
        if num < lowest:
            lowest = num
    
    length = len(numbers)

    return total , highest , lowest , length

numbers = [5,2,8,1,9,3]

total , hightest , lowest , length = analyze_list(numbers)





print(f"sum : {total}")
print(f"length : {length}")
print(f"lowest : {lowest}")
print(f"hightest : {hightest}")