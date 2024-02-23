items = input().split('|')
stealed_items = []
avg_treasures = 0
while True:
    command = input()

    if command == 'Yohoho!':
        if len(items) == 0:
            print(f'Failed treasure hunt.')
            break
        else:
            for f in items:
                avg_treasures += len(f)
            avg_treasures /= len(items)
            print(f'Average treasure gain: {avg_treasures:.2f} pirate credits.')
            break

    command = command.split()

    if command[0] == 'Loot':
        for x in range(1, len(command)):
            if command[x] not in items:
                items.insert(0, command[x])
    elif command[0] == 'Drop':
        index = int(command[1])
        if 0 <= index < len(items):
            item = items.pop(index)
            items.append(item)
    elif command[0] == 'Steal':
        count = int(command[1])
        stealed_items = items[-count:] if count < len(items) else items[:]
        items = items[:-count] if count < len(items) else []
        print(', '.join(stealed_items))
        stealed_items = []
