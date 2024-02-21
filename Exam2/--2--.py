def main_func(numbers):
    while True:
        command = input()

        if command == 'end':
            numbers = [str(i) for i in numbers]
            main_list = ', '.join(numbers)
            print(main_list)
            break

        command = command.split()

        if command[0] == 'swap':
            swaping_index1 = numbers[int(command[1])]
            swaping_index2 = numbers[int(command[2])]
            numbers[int(command[1])] = swaping_index2
            numbers[int(command[2])] = swaping_index1
        elif command[0] == 'multiply':
            multiply_index1 = numbers[int(command[1])]
            multiply_index2 = numbers[int(command[2])]
            product = multiply_index1 * multiply_index2
            numbers.pop(int(command[1]))
            numbers.insert(int(command[1]), product)
        else:
            numbers = [i - 1 for i in numbers]


numbers = list(map(int, input().split()))

main_func(numbers)
