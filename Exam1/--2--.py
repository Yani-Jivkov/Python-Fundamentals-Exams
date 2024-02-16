targets = list(map(int, input().split()))
shot_targets = 0

while True:
    command = input()

    if command == 'End':
        targets_str = ' '.join(str(x) for x in targets)
        print(f'Shot targets: {shot_targets} -> {targets_str}')
        break

    index = int(command)

    if 0 <= index < len(targets) and targets[index] != -1:
        current_target_value = targets[index]
        targets[index] = -1
        shot_targets += 1

        for i in range(len(targets)):
            if targets[i] == -1:
                continue
            if targets[i] > current_target_value:
                targets[i] -= current_target_value
            else:
                targets[i] += current_target_value

2@4@2
Jump 2
Jump 2
Jump 8
Jump 3
Jump 1
Love!
