def total(coins):
    out = 0
    value = [200, 100, 50, 20, 10, 5, 2, 1]
    for x in xrange(0, 8):
        out += coins[x] * value[x]
    return out

def change(n, coins):
    if n < 0:
        return []
    if n == 0:
        return [[]]
    all_changes = []

    for coin in coins:
        combos = change(n - coin, coins)
        for combo in combos:
            combo.append(coin)
            all_changes.append(combo)
    return all_changes

def main():
    print change(200, [200, 100, 50, 20, 10, 5, 2, 1])

main()

