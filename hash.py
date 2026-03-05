const crypto = require('crypto');


function msg_to_integer(msg) {
  // Given a hex string to sign, convert that string to a Buffer of bytes,
  // double-SHA256 the bytes and then return a BigInt() from the 32-byte digest.
 
  // Convert hex string to Buffer
  const buffer = Buffer.from(msg, 'hex');
 
  // First SHA256 hash
  const hash1 = crypto.createHash('sha256').update(buffer).digest();
 
  // Second SHA256 hash (double-SHA256)
  const hash2 = crypto.createHash('sha256').update(hash1).digest();
 
  // Convert the 32-byte digest to BigInt
  // Use 'hex' to get hex string, then convert to BigInt with '0x' prefix
  const hashHex = hash2.toString('hex');
  const integer = BigInt('0x' + hashHex);
 
  return integer;
}
