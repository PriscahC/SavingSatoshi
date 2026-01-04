# Chapter 3: Mining Pools & 51% Attacks

## Understanding 51% Attacks

**Scenario:** Bitcoin is being hit with a 51% attack! After you brought mining devices online, Vanderpoole turned BitRey's ASICs back on and is mining empty blocks.

**Solution:** Place a unique identifier in the **extraNonce** when preparing block data to prevent duplicate mining efforts among pool participants.

---

## What is the ExtraNonce?

In the **Stratum mining pool protocol** (not Bitcoin protocol), the coinbase transaction contains an **extra nonce** field. Mining pools divide this into two parts:

- **extranonce1** - Assigned by the pool to each miner
- **extranonce2** - Updated by individual miners

### Why Split the ExtraNonce?

**Advantages of this approach:**

1. **Prevents Duplicate Work** - Each miner has a unique extranonce1, ensuring no two miners perform identical computations

2. **Efficient Data Distribution** - The pool can send the same transaction list to all miners. Miners only need to update extranonce2, not rebuild the entire block

3. **Contribution Tracking** - The extranonce1 allows pools to identify and determine each miner's share contribution

### How Miners Use ExtraNonce

The mining process works as follows:

1. Miner receives extranonce1 from the pool
2. Miner cycles through the nonce in the block header
3. Miner updates extranonce2 as needed
4. If no solution is found, repeat with a different extranonce2
5. Continue until a valid block is discovered

---

## 💰 Mining Pool Rewards

When a block is mined, the reward is distributed among pool participants. The total reward consists of:

### 1. Transaction Fees
All fees from transactions included in the block

### 2. Block Subsidy
The fixed amount of new bitcoin created with each block

### Reward Distribution Metrics

Pools calculate individual miner rewards based on:

- **Hash Rate Percentage** - Your computational power relative to the pool
- **Block Found Percentage** - Your contribution to successfully mined blocks
- **Partial Solution Percentage** - Your share submissions (proof of work)

---

*This chapter demonstrates how mining pools coordinate distributed mining efforts and defend against attacks through efficient work distribution.*
