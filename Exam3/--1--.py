n = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

total = 0

for i in range(1, n + 1):
    total += daily_plunder
    if i % 3 == 0:
        total += daily_plunder / 2
    if i % 5 == 0:
        total *= 0.7

if total >= expected_plunder:
    print(f'Ahoy! {total:.2f} plunder gained.')
else:
    print(f'Collected only {(total * 100) / expected_plunder:.2f}% of the plunder.')
