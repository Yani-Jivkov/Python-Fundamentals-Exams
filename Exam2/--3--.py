def main_func(journal):
    while True:
        command = input()

        if command == 'Craft!':
            journal = [str(i) for i in journal]
            main_list = ', '.join(journal)
            print(main_list)
            break

        command = [i for i in command.split(' - ')]

        if command[0] == 'Collect':
            if command[1] in journal:
                continue
            else:
                journal.append(command[1])
        elif command[0] == 'Drop':
            if command[1] in journal:
                journal.remove(command[1])
        elif command[0] == 'Combine Items':
            old_new_item = command[1]
            old_new_item = [i for i in old_new_item.split(':')]
            if old_new_item[0] in journal:
                old_item_place = journal.index(old_new_item[0])
                journal.insert(old_item_place + 1, old_new_item[1])
        else:
            if command[1] in journal:
                journal.remove(command[1])
                journal.append(command[1])

journal = [i for i in input().split(', ')]

main_func(journal)
