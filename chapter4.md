# Chapter 4: Key Pairs 🔑

A single **key pair** is all that’s needed to create a Bitcoin wallet and control the funds within it.

- **Private key** → used to **spend** bitcoin  
- **Public key** → used to **receive** bitcoin  

---

## How Do We Generate a Public Key?

To generate a public key, we rely on **Elliptic Curve Cryptography (ECC)**.

Bitcoin uses a specific elliptic curve called **secp256k1**, defined by the equation:

```

y² = x³ + 7

````

ECC works by performing mathematical operations on points that lie on this curve.

---

## The Generator Point

Bitcoin starts with a special, fixed point on the curve known as the **Generator Point (G)**:

```js
G = {
  x: 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
  y: 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
}
````

This point is defined by the **secp256k1 standard** and is always the same.

---

## Deriving a Public Key

To derive a public key from a private key:

```
P = k * G
```

Where:

* `k` is the **private key**
* `G` is the **generator point**
* `P` is the resulting **public key**

This operation involves repeated elliptic curve addition, similar to multiplication.

---

## Implementing `privateKeyToPublicKey()`

The function below accepts a private key (hex-encoded) and returns a **Group Element (GE)** representing the public key.

```js
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
(
  5197ffde3b6afa4b54724e0e3dd431046017aaee88af65a1a8bcef98b7431c3d,
  f1831a619d2fa2dedb29c8a49409453cd13b3bf2ff319e6328604c30eacaa797
)
```

**Evaluation:**
Good job! That public key is pretty long. Let’s compress it.

---

## Compressing the Public Key

An uncompressed public key contains:

* 32 bytes for `x`
* 32 bytes for `y`

We can compress it into **33 bytes** by:

* Keeping the `x` coordinate
* Adding **one metadata byte**:

  * `02` if `y` is **even**
  * `03` if `y` is **odd**

Because the curve equation has only two solutions for `y`, the full key can later be reconstructed.

---

## Implementing `compressPublicKey()`

```js
const uncompressedKey = [
  "5197ffde3b6afa4b54724e0e3dd431046017aaee88af65a1a8bcef98b7431c3d",
  "f1831a619d2fa2dedb29c8a49409453cd13b3bf2ff319e6328604c30eacaa797"
]

// Determine if the y coordinate is even or odd and prepend the
// corresponding header byte to the x coordinate.
// Return a hex string
function compressPublicKey(publicKey) {
  const header_byte = {
    y_is_even: '02',
    y_is_odd: '03'
  }

  const [x, y] = publicKey
  const yBigInt = BigInt('0x' + y)

  const header =
    yBigInt % 2n === 0n
      ? header_byte.y_is_even
      : header_byte.y_is_odd

  return header + x
}
```

### Result

```
035197ffde3b6afa4b54724e0e3dd431046017aaee88af65a1a8bcef98b7431c3d
```

✅ **Evaluation:**
Excellent. Now we have our compressed public key.

---

## Hashing the Compressed Public Key

Bitcoin uses **two hashing algorithms**:

1. **SHA-256**
2. **RIPEMD-160**

This produces a **20-byte public key hash**.

> Generating a public key is a **one-way operation**.
> Recovering the private key would require solving the **discrete logarithm problem**, which is computationally infeasible.

---

## Implementing `hashCompressed()`

```js
const crypto = require('crypto')

// Get the sha256 digest of the compressed public key.
// Then get the ripemd160 digest of that sha256 hash
// Return 20-byte hex string
function hashCompressed(compressedPublicKey) {
  const sha256 = crypto
    .createHash('sha256')
    .update(Buffer.from(compressedPublicKey, 'hex'))
    .digest()

  const ripemd160 = crypto
    .createHash('ripemd160')
    .update(sha256)
    .digest('hex')

  return ripemd160
}

module.exports = hashCompressed
```

### Result

```
d5f796e6255c11dd4555ca48f19a90cc87eade60
```

✅ **Evaluation:**
Great. One more step and you will have your wallet address.

---

## Creating a P2WPKH Address (Bech32)

We now encode the hash into a **Pay-to-Witness-Public-Key-Hash (P2WPKH)** address.

### Steps:

1. Prepend witness version `0`
2. Encode using **bech32**
3. Add a human-readable prefix (HRP)

| Network | Prefix |
| ------- | ------ |
| Mainnet | `bc`   |
| Testnet | `tb`   |
| Regtest | `bcrt` |

---

## Implementing `hashToAddress()`

```js
const bech32 = require('@savingsatoshi/bech32js')

const compressedPublicKeyHash = Buffer.from(
  '775ae3680dc50210f3ca78df9580b4b2110dc67c',
  'hex'
)

// Insert checksum and metadata, encode using bech32 and return a string
function hashToAddress(hash) {
  const version = 0       // Witness version
  const hrp = 'tb'        // Testnet prefix

  const data = Array.from(hash)
  const address = bech32.encode(hrp, version, data)

  return address
}
```

### Result

```
tb1qwadwx6qdc5pppu720r0etq95kggsm3nu27aq4c
```

✅ **Evaluation:**
You now have a valid **Bitcoin Testnet P2WPKH address** 🎉

---

> **End of Chapter 4**
> *Next: Chapter 5 - Don't trust, Verify.*

```
