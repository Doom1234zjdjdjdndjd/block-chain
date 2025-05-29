# block-chain
 Simple blockchain implementation in Python

 # Simple Blockchain in Python

This is a basic implementation of a blockchain using Python for educational purposes

## Block Structure

Each block contains
- Index
- Timestamp
- Data
- Previous hash
- Nonce (used for proof-of-work)
- Its own hash

## How It Works

- The first block is the Genesis block
- New blocks are added with a basic proof-of-work mechanism
- Each block's hash must start with two zeroes ("00")
- The blockchain is a list of such blocks

## Validation

The `is_chain_valid()` function checks that
- Each block’s stored hash is correct
- The previous hash value matches the hash of the previous block

## Proof-of-Work

A nonce is found by looping until the hash of the block starts with two zeros. This simulates how mining works in real blockchains.

