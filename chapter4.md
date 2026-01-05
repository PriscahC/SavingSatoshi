# Chapter 4: Cryptographic Key Pairs & Wallets

## Understanding Key Pairs

A single key pair is all that's needed to create a wallet and control the funds within it.

- **Private Key** → Used when you want to **spend** bitcoin
- **Public Key** → Used when you want to **receive** bitcoin

---

## 📐 Elliptic Curve Cryptography (ECC)

### How Do We Generate a Public Key?

Bitcoin uses a fascinating branch of cryptography called **Elliptic Curve Cryptography (ECC)**. This involves taking certain points on an elliptic curve and performing addition and multiplication operations on those points.

### Bitcoin's Curve: secp256k1

Bitcoin uses a specific curve called **secp256k1**, defined by the equation:

```
y² = x³ + 7
```

We start with a specific point on this curve called the **Generator Point (G)**.

### The Generator Point

The generator point is a constant value defined in the secp256k1 standard:

```javascript
G = {
  x: 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
  y: 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
}
```

### Deriving the Public Key

To derive a public key from a private key, we perform an elliptic curve operation repeatedly with the generator point.

Mathematical operations on an elliptic curve are similar to addition. Therefore, repetition of those operations is similar to multiplication:

```
P = k × G
```

Where:
- **P** = Public Key
- **k** = Private Key
- **G** = Generator Point

---

## Coding Challenge: Private Key to Public Key

**Task:** Complete the function `privateKeyToPublicKey()` which accepts a private key as a hex-encoded string and returns the corresponding public key as a GE (Group Element) object.

### Solution Code

```javascript
const secp256k1 = require('@savingsatoshi/secp256k1js')

// Generator point
const G = secp256k1.G

function privateKeyToPublicKey(privateKey) {
  // Convert hex string private key to BigInt
  const encodedPrivateKey = BigInt('0x' + privateKey)
  
  // Multiply generator point G by the private key
  const publicKeyPoint = G.mul(encodedPrivateKey)
  
  // Return the curve point (secp256k1.GE)
  return publicKeyPoint
}

module.exports = privateKeyToPublicKey
```

### Result

```
(5197ffde3b6afa4b54724e0e3dd431046017aaee88af65a1a8bcef98b7431c3d, 
 f1831a619d2fa2dedb29c8a49409453cd13b3bf2ff319e6328604c30eacaa797)
```

✅ **Success!** The public key was generated correctly.

---

## 🗜️ Public Key Compression

### The Problem

The public key has an **x** and **y** coordinate for a total of **64 bytes**. That's pretty long!

### The Solution

Compress it into **33 bytes** by:
1. Removing the y coordinate
2. Prepending a single byte of metadata

### How It Works

The metadata byte indicates if the Y coordinate is **even** or **odd**:
- Metadata byte = `'02'` if y is **even**
- Metadata byte = `'03'` if y is **odd**

Because the elliptic curve equation only has two variables, the complete public key can be computed later by the verifier using only **x** and the **metadata**:

```
y² = x³ + 7
```

### Coding Challenge: Compress the Public Key

**Task:** Complete the function `compressPublicKey()` to accept a public key and return a 33-byte hex string representing the compressed public key.

```javascript
function compressPublicKey(publicKey) {
  // Extract x coordinate
  const x = publicKey.x.toString(16).padStart(64, '0')
  
  // Determine if y is even or odd
  const prefix = publicKey.y.isEven() ? '02' : '03'
  
  // Return compressed public key: prefix + x coordinate
  return prefix + x
}
```

---

*This chapter explores the mathematical foundation of Bitcoin's cryptographic security through elliptic curve operations.*
