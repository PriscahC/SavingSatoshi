# Chapter 2: Mining & Cryptographic Hashing

## ⚙️ Mining Hardware

Modern Bitcoin mining is performed by machines with a special chip called an **Application-Specific Integrated Circuit (ASIC)**. These specialized processors are designed exclusively for the computational demands of Bitcoin mining.

---

## Understanding Hash Functions

### What Are Hashes?

**Hash functions are one-way streets.** You can't reverse engineer a hash to figure out the data used to make it.

Hashes are extremely reliable in the sense that they are **deterministic**. This means you can hash the same piece of data over and over again and you'll always get the same result.

---

## SHA-256 in Bitcoin

**SHA-256** is a crucial component in Bitcoin's cryptographic processes. It is used in several ways:

### 1. **Hashing Transactions**
Every transaction in the Bitcoin network is hashed using SHA-256 to create a unique transaction ID. This ensures the integrity and immutability of the transaction data.

### 2. **Block Hashing**
In mining, SHA-256 is used in the Proof of Work algorithm. Miners repeatedly hash block headers with varying nonce values until they find a hash that meets the network's difficulty target, producing a valid block.

### 3. **Address Generation**
When creating a Bitcoin address, the public key is first hashed using SHA-256, and then RIPEMD-160 to produce the final address. This two-step hashing process enhances security by making it more difficult to reverse-engineer the original public key from the Bitcoin address.

### 4. **Security Against Length Extension Attacks**
Bitcoin uses a double hashing method (**SHA-256d**) to prevent length extension attacks. This involves hashing the result of an initial SHA-256 hash again using SHA-256.

---

## Mining Challenge Examples

### Hash that starts with **one zero**

| Input | Output Hash Preview |
|-------|---------------------|
| Abracadabr | 002891c72a3037c8a74959c92229a11563393e51dfbf4b3cbef5221904f21e81 |
| popcorn | 0a4ef253e3fef22cb9d3bc5280386f9f2d1cf351da6582d8254659d1b27ea0b3 |

### Hash that starts with **two zeros**

| Input | Output Hash Preview |
|-------|---------------------|
| trigonometry | 00485d196a5d797f300be21ce5be3d066a0f988730b6d0c1934dfb83d582c93a |

---

## Build Your Own Hash Function

### Challenge: Find a Hash Starting with Five Zeros

Write a script that generates a SHA-256 hash that begins with five zeroes (`"00000..."`).

**Resources:**
- [Node.js Crypto createHash Method](https://www.geeksforgeeks.org/node-js/node-js-crypto-createhash-method/)
- [Node.js Crypto Documentation](https://www.educative.io/answers/what-is-node-cryptocreatehashalgorithm-options)

### Solution Code

```javascript
const crypto = require('crypto');

function findHashFromNonce(nonce) {
  while (true) {
    const hash = crypto
      .createHash('sha256')
      .update(nonce.toString())
      .digest('hex');
    
    if (hash.startsWith('00000')) {
      return nonce; // ✅ return the nonce
    }
    
    nonce++;
  }
}

// Example usage
findHashFromNonce(0);
```

### How It Works

1. **Initialize** a nonce value starting at 0
2. **Hash** the nonce using SHA-256
3. **Check** if the hash starts with five zeros
4. **Increment** the nonce and repeat until a valid hash is found
5. **Return** the successful nonce value

> **Note:** This process demonstrates the computational work required in Bitcoin mining. Finding hashes with more leading zeros requires exponentially more attempts.

---

## ⛏️ Mining Simulation: See It In Action

Now that we know how mining works, let's see it in action!

### Simulation Parameters

**Current Network Requirements:**
- Hash must have **10 leading zeros**
- Each block contains **3,500 transactions**
- Rewards and fees: **0.061 BTC** per block

https://github.com/user-attachments/assets/822f79c3-0ce5-4df5-b3dc-6a2e252fbe80

*Watch the mining process in real-time as blocks are discovered*

### 📊 Simulation Results

After mining **100 blocks**, here's what we achieved:

**Transactions Confirmed:**
- **350,000 total transactions** processed
- (100 blocks × 3,500 transactions per block)

**Mining Rewards Collected:**

You've collected a nice reward for all this mining! Your earnings consist of:

1. **Block Subsidy** - The amount of bitcoin the network rewards for each block
2. **Transaction Fees** - Additional income collected from users sending transactions

> 💰 **Total Earnings:** The combination of block subsidies and transaction fees provides the economic incentive that keeps miners securing the network.

---

*This exercise illustrates the Proof of Work mechanism that secures the Bitcoin network and demonstrates how miners are compensated for their computational work.*
