# My Bitcoin Core Challenge Journey

## Day's Summary
Today I didn't save any Satoshis.

I was doing the Bitcoin Core challenge and it wasn't easy.

## Setting Up WSL and Development Environment

First, since I don't yet use Ubuntu, I had to install on WSL. That was the easiest part.

Then I created a dev user and a password.

## Cloning the Repository - Authentication Issues

I cloned the repo with HTTPS but it wasn't working, also because it was a private repo and I hadn't authenticated myself. 

### Installing GitHub CLI
So I used:
```bash
gh auth login
```

The prompts were flawless since it prompted me to install gh with sudo, then I logged in.

Okay, now cloning the repo with HTTPS wasn't working.

### Generating SSH Key
So on my terminal, I generated the public key with:
```bash
ssh-keygen -t ed25519 -C opiyopriscah4@gmail.com
```

This creates a new SSH key, using the provided email as a label.
```
> Generating public/private ALGORITHM key pair.
```

When prompted to "Enter a file in which to save the key", I pressed Enter to accept the default file location:
```
> Enter file in which to save the key (/c/Users/YOU/.ssh/id_ALGORITHM):[Press enter]
```

At the prompt for a secure passphrase I left it empty:
```
> Enter passphrase (empty for no passphrase): [Type a passphrase]
> Enter same passphrase again: [Type passphrase again]
```

**Resource used:** [GitHub SSH Key Generation Guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

Done.

### Adding SSH Key to GitHub
So once I did that, I went to GitHub:
1. On my profile, selected **Settings**
2. Then **SSH and GPG keys**
3. Then I added a new SSH key by pasting the public key I had generated

Done.

### Switching to SSH Protocol
I switched to my preferred protocol, SSH:
```bash
gh config set git_protocol ssh
```

Then:
```bash
gh auth refresh -s write:public_key
```

When I cloned again with SSH it worked:
```bash
git clone sshlink
```

**Gemini helped with most of the troubleshooting.**

## Building Bitcoin Core

Now with that done, next step is building the Bitcoin Core so I can run the tests locally on my laptop.

### Step 1: Install Dependencies
```bash
sudo apt-get update
sudo apt-get install build-essential libtool autotools-dev automake pkg-config bsdmainutils python3
sudo apt-get install libevent-dev libboost-system-dev libboost-filesystem-dev libboost-test-dev libboost-thread-dev
```

### Step 2: Initial Build Attempt
```bash
# Move into the repo
# cd bitcoin-core-test-the-test-PriscahC

# Generate build files
./autogen.sh

# Configure with minimal features (disables wallet, GUI, and other features)
./configure --disable-wallet --disable-gui --disable-tests --disable-bench --without-miniupnpc

# Build (use -j to speed up with multiple cores)
make -j$(nproc)
```

This made my WSL keep stopping, so I had to use one core.

### Step 3: CMake Build (Single Core)
```bash
cd ~/home/bitcoin-core-test-the-test-PriscahC/bitcoin/build
rm -rf *
cmake .. -DBUILD_WALLET=OFF -DBUILD_GUI=OFF -DENABLE_IPC=OFF -DWITH_ZMQ=OFF
cmake --build . -j1
```

Still running...

## Next Steps

So now what I'm working on is making this build, then I get to run the tests locally, test them. Then once they're okay, I push it to GitHub. But on second thought, I can just be doing it on the GUI.

### Code Changes
Added lines 125 to 127 in `bitcoin/wallet.cpp`.

It didn't work.

### Resources Used
- [Bitcoin Core Testing Documentation](https://github.com/boss-2026-challenge/bitcoin-core-test-the-test-PriscahC/blob/main/bitcoin/test/README.md#running-tests-locally)
- Claude (for running tests locally)

---

*Journey in progress...*
