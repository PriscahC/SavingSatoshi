# Bitcoin Learning Journey 🚀

A hands-on exploration of Bitcoin's technical foundations through practical exercises and simulations.

---

## What I've Learned

### Chapter 1: The Genesis Block
- Decoded the Genesis Block's coinbase message using hex-to-ASCII conversion
- Discovered Satoshi's embedded newspaper headline: *"The Times 03/Jan/2009 Chancellor on brink of second bailout for banks"*
- Explored OP_RETURN for storing messages on the blockchain

### Chapter 2: Mining & Cryptography
- Built a Node.js mining script to find SHA-256 hashes with five leading zeros
- Understood how Proof of Work secures the network through computational difficulty
- Simulated mining 100 blocks, processing 350,000 transactions
- Learned about miner economics: block subsidies + transaction fees

### Chapter 3: Mining Pools & 51% Attacks
- Experienced a simulated 51% attack scenario with empty block mining
- Learned about the Stratum protocol and extraNonce mechanism
- Understood how mining pools coordinate work distribution (extranonce1 & extranonce2)
- Explored reward distribution: transaction fees + block subsidy
- Studied pool metrics: hash rate percentage, block found percentage, partial solution percentage

### Chapter 4: Cryptographic Key Pairs & Wallets
- Learned about Elliptic Curve Cryptography (ECC) and the secp256k1 curve
- Understood the Generator Point (G) and the equation y² = x³ + 7
- Built a function to derive public keys from private keys (P = k × G)
- Implemented public key compression (64 bytes → 33 bytes)
- Learned about metadata bytes for storing even/odd y-coordinate information

### Chapter 5: Digital Signatures & Verification
- Discovered Satoshi's signature in Block #170 (first transaction to Hal Finney)
- Located Satoshi's public key in the Block #9 coinbase transaction
- Built transaction messages using Bitcoin's signing algorithm
- Implemented double SHA-256 hashing to prevent length-extension attacks
- Decoded DER-encoded signatures to extract R and S values
- Successfully verified Satoshi's ECDSA signature using elliptic curve mathematics

---

## Skills Gained
- Command line hex decoding (`xxd`)
- Node.js crypto library (hashing, ECDSA operations)
- Elliptic Curve Cryptography and point multiplication
- DER signature encoding/decoding
- Bitcoin transaction structure and signing algorithms
- ECDSA signature verification implementation
- Understanding hash functions and deterministic properties
- Mining pool coordination protocols (Stratum)

---

## Next Steps
- Chapter 5.2: Validating the signature

---

*Last Updated: January 2026*
