houses = list(map(int, input().split('@')))
cupid_position = 0
helper = 0

while True:
    jump = input()

    if jump == 'Love!':
        break
    else:
        length = int(jump.split()[1])
        cupid_position += length

        if cupid_position >= len(houses):
            cupid_position = 0

        if houses[cupid_position] > 0:
            houses[cupid_position] -= 2
            if houses[cupid_position] == 0:
                print(f'Place {cupid_position} has Valentine\'s day.')
                helper += 1
        else:
            print(f'Place {cupid_position} already had Valentine\'s day.')

failed_houses = len([house for house in houses if house > 0])

print(f'Cupid\'s last position was {cupid_position}.')
if failed_houses == 0:
    print('Mission was successful.')
else:
    print(f'Cupid has failed {failed_houses} places.')
