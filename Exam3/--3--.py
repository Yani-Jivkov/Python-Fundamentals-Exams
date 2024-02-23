pirate_ship_status = list(map(int, input().split('>')))
war_ship_status = list(map(int, input().split('>')))
maximum_health = int(input())
sections_need_repair = 0
pirate_ship = 0
war_ship = 0
helper = 0

while True:
    command = input()

    if command == 'Retire':
        if helper >= 1:
            break
        else:
            pirate_ship = sum(pirate_ship_status)
            war_ship = sum(war_ship_status)
            print(f'Pirate ship status: {pirate_ship}')
            print(f'Warship status: {war_ship}')
            break

    parts = command.split()
    action = parts[0]

    if action == 'Fire':
        index, damage = int(parts[1]), int(parts[2])
        if 0 <= index < len(war_ship_status):
            war_ship_status[index] -= damage
            if war_ship_status[index] <= 0:
                print('You won! The enemy ship has sunken.')
                helper = 1
                break

    elif action == 'Defend':
        start_index, end_index, damage = int(parts[1]), int(parts[2]), int(parts[3])
        if 0 <= start_index < len(pirate_ship_status) and 0 <= end_index < len(pirate_ship_status):
            for i in range(start_index, end_index + 1):
                pirate_ship_status[i] -= damage
                if pirate_ship_status[i] <= 0:
                    print('You lost! The pirate ship has sunken.')
                    helper = 1
                    break
            if helper == 1:
                break

    elif action == 'Repair':
        index, health = int(parts[1]), int(parts[2])
        if 0 <= index < len(pirate_ship_status):
            pirate_ship_status[index] += health
            if pirate_ship_status[index] > maximum_health:
                pirate_ship_status[index] = maximum_health

    elif action == 'Status':
        sections_need_repair = sum(1 for section in pirate_ship_status if section < maximum_health * 0.2)
        print(f"{sections_need_repair} sections need repair.")
