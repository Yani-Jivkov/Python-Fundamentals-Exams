def main_calc(energy):
    won_battles = 0

    while True:
        distance = input()
        if distance == "End of battle":
            print(f"Won battles: {won_battles}. Energy left: {energy}")
            break
        distance = int(distance)
        if energy >= distance:
            energy -= distance
            won_battles += 1
            if won_battles % 3 == 0:
                energy += won_battles
        else:
            print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
            break

energy = int(input())

main_calc(energy)


