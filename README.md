# 2024-Spring-HW2

## 3.3
Please complete the report problem below:

### Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution
path: tokenB-> tokenA-> tokenE-> tokenD-> tokenC-> tokenB
swap1 (tokenB: 5                 ether, tokenA: 5.666666666666667 ether)
swap2 (tokenA: 5.666666666666667 ether, tokenE: 1.0625            ether)
swap3 (tokenE: 1.0625            ether, tokenD: 2.44604316547     ether)
swap4 (tokenD: 2.44604316547     ether, tokenC: 5.0796812749      ether)
swap5 (tokenC: 5.0796812749      ether, tokenB: 20.1404124616     ether)
tokenB balance: 20.1404124616 ether

### Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Solution
Slippage is the difference in price between when a trade is submitted and when it's executed. Uniswap V2 addresses this by allowing users to set a minimum amount out parameter. If the trade can't satisfy this minimum due to price movement, it reverts.
Example function to illustrate:
swapExactTokensForTokens(amountIn, amountOutMin, path, to, deadline);

### Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution
The Uniswap V2 protocol subtracts a minimum liquidity amount (specifically, the MINIMUM_LIQUIDITY which is 1000 tokens) upon the first liquidity provision to a new pool. This is done to prevent rounding errors when the pool is initialized. If the initial liquidity provision was extremely small, rounding errors could disproportionally affect prices. To avoid these small pools, the protocol locks the minimum liquidity, which is sent to the address 0. 

### Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution
When minting liquidity tokens (other than the initial provision), the liquidity minted is proportional to the existing liquidity in the pool. The formula ensures that the liquidity is added in a ratio that preserves the current price. If this weren't the case, liquidity providers could significantly impact the price by adding liquidity, which is not the intention—instead, they are meant to provide depth to the market without affecting the price. The calculation is done based on Uniswap's constant product formula (x * y = k), ensuring that the product of the reserves is constant after any transaction.

### Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution
A sandwich attack is when an attacker sees a pending trade(yout trade), typically one with significant market impact, and places orders before and after it. This can result in the initial trader(you) getting a worse price. This attack relies on the ability to order transactions and exploit trade slippage.

## 3.4
### Bonus
My path(as in Problen 1 above) is the most profitable path among all possible swap paths. Python script included. 