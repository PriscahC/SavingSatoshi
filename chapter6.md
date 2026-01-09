# Chapter 6

---

"This might make me sound stupid, but are you the real Satoshi?"

**HOLOCAT:** "Hardly the only thing to make you sound stupid lately."

---

Bitcoin is defined by its community and cannot be co-opted by a single individual or entity—including Satoshi.

---

## Understanding Unspent Transaction Outputs (UTXOs)

This is an unspent transaction output (aka "UTXO"). You might recognize your compressed public key hash and address from chapter 4. The amount looks right, too: 1.61 BTC.

```bash
$ bitcoin-cli listunspent
[
  {
    "txid": "74149a689ce95562309cf4c404ef6ca91e76b6a19ef25e9625e9c13d93fac4e1",
    "vout": 0,
    "address": "bc1qm2dr49zrgf9wc74h5c58wlm3xrnujfuf5g80hs",
    "label": "",
    "scriptPubKey": "0014da9a3a9443424aec7ab7a628777f7130e7c92789",
    "amount": 1.61000000,
    "confirmations": 341,
    "spendable": true,
    "solvable": true,
    "desc": "wpkh([a73804d3/0'/0'/0']02ab3d3cb82c1eb89168824b20f667224d868250dedec69177012e5a26c5221ae8)#5mf00k95",
    "parent_descs": [
    ],
    "safe": true
  }
]
```

---

## Sending Bitcoin

Mika 3000 gives you an address to send your 1 BTC contribution to:

```
bc1qgghq08syehkym52ueu9nl5x8gth23vr8hurv9dyfcmhaqk4lrlgs28epwj
```

Why is it longer than yours?

---

## Creating a Segregated Witness Transaction

We need to create and sign a transaction that sends one of your 1.61 BTC to this address. We'll be using a protocol called **Segregated Witness** which sets the transaction version to 2.

Segregated Witness transactions work just like their legacy predecessors. There are a few global values like version and locktime. There is an array of inputs (UTXOs we want to spend) and an array of outputs (new UTXOs we want to create, for other people to spend in the future). There will also be an array of witnesses, one for each input. That is where signatures and scripts will go instead of the scriptSig.

The message serializations for all these components is documented here:
- [Protocol documentation #tx](https://en.bitcoin.it/wiki/Protocol_documentation#tx)
- [Bitcoin Book - Transactions](https://github.com/bitcoinbook/bitcoinbook/blob/6d1c26e1640ae32b28389d5ae4caf1214c2be7db/ch06_transactions.adoc)

---

**Image:** The input class implementation
