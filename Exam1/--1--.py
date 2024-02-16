def main_func():
    taxes = 0
    total_price = 0
    while True:
        part_price = input()

        if part_price == 'special' or part_price == 'regular':
            prints(part_price, total_price, taxes)
            break
        else:
            part_price = float(part_price)
            if part_price <= 0:
                print(f'Invalid price!')
                continue

            helper = part_price * 0.2
            taxes += helper
            total_price += part_price

def prints(part_price, total_price, taxes):
    if part_price == 'special':
        if total_price == 0:
            print(f'Invalid order!')
        else:
            print(f'Congratulations you\'ve just bought a new computer!')
            print(f'Price without taxes: {total_price:.2f}$')
            print(f'Taxes: {taxes:.2f}$')
            print(f'-----------')
            print(f'Total price: {(total_price + taxes) * 0.9:.2f}$')
    elif part_price == 'regular':
        if total_price == 0:
            print(f'Invalid order!')
        else:
            print(f'Congratulations you\'ve just bought a new computer!')
            print(f'Price without taxes: {total_price:.2f}$')
            print(f'Taxes: {taxes:.2f}$')
            print(f'-----------')
            print(f'Total price: {total_price + taxes:.2f}$')

main_func()

