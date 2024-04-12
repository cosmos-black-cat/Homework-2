liquidity = {
    ("tokenA", "tokenB"): (17, 10), # 17a = 10b  a = 10b/17                 10/17
    ("tokenA", "tokenC"): (11, 7), # 11a = 7c    c = 11a/7 = 11/7*10/17 b   110/119
    ("tokenA", "tokenD"): (15, 9), # 15a = 9d    d = 5a/3  = 5/3 *10/17 b   
    ("tokenA", "tokenE"): (21, 5), # 21a = 5e    e = 21a/5 = 21/5*10/17 b
    ("tokenB", "tokenC"): (36, 4), # 36b = 4c    c = 9b
    ("tokenB", "tokenD"): (13, 6), # 13b = 6d    d = 13b/6
    ("tokenB", "tokenE"): (25, 3), # 25b = 3e    e = 25b/3
    ("tokenC", "tokenD"): (30, 12), # 30c = 12d  d = 5c/2  = 5/2*9 b
    ("tokenC", "tokenE"): (10, 8), # 10c = 8e    e = 5c/4  = 5/4*9 b
    ("tokenD", "tokenE"): (60, 25), # 60d = 25e  e = 12d/5 = 12/5*5/2*9 b
}

def calculate_rate(amount, x_liquidity, y_liquidity):
    return y_liquidity - (y_liquidity * x_liquidity / (x_liquidity + amount))

def direct_exchange(tokenX, tokenY, amount):
    if (tokenX, tokenY) in liquidity:
        x_liquidity, y_liquidity = liquidity[(tokenX, tokenY)]
        return calculate_rate(amount, x_liquidity, y_liquidity) 
    elif (tokenY, tokenX) in liquidity:
        y_liquidity, x_liquidity = liquidity[(tokenY, tokenX)]
        return calculate_rate(amount, x_liquidity, y_liquidity)
    else:
        return 0  # No direct pair exists

def check_arbitrage_cycle(cycle, amount):
    initial_amount = amount
    for i in range(len(cycle) - 1):
        tokenX, tokenY = cycle[i], cycle[i + 1]
        amount = direct_exchange(tokenX, tokenY, amount)
    return amount

def find_arbitrage_opportunities():
    tokens = ["tokenA", "tokenC", "tokenD", "tokenE"]
    tokenB = "tokenB"
    best_profit = 0
    best_cycle = []
    for first_token in tokens:
        for second_token in tokens:
            if second_token == first_token: continue
            for third_token in tokens:
                if third_token in [first_token, second_token]: continue
                for fourth_token in tokens:
                    if fourth_token in [first_token, second_token, third_token]: continue
                    cycle = [tokenB, first_token, second_token, third_token, fourth_token, tokenB]
                    tmp = check_arbitrage_cycle(cycle, 5)
                    if tmp > best_profit:
                        best_profit = tmp
                        best_cycle = cycle
    if best_profit >= 20:
        path_str = '->'.join(best_cycle)
        print(f"path: {path_str}, tokenB balance= {best_profit}")
find_arbitrage_opportunities()