# claymore

```
                 \.          claymore
-===============-{]###=<>    encrypted p2p chat client
                 /'          
```

# Installation

Clone the repository, cd into it, then run:

```
# pip install .
```

You can install it without root, but you might need to mess around with your `PATH` variable.


# Usage

```
# claymore <host>:<port> <password>
```

claymore must be ran as root.

Since claymore is p2p, if you have a router in between you and the other client, some port-forwarding may be needed.


# Security

On execution your password is hashed with pbkdf2.

When ever you send/receive a message, your hashed password is salted with the number of messages you have sent or received, then hashed with sha256.

That sha256 hash is then used as your key to encrypt/decrypt that message using AES.

With this model, every message is encrypted with a different AES key that is never sent over the wire.

I'm not sure if this is totally secure, an it most certainly isn't the best method, but this project is more of me messing around with/learning basic cryptography.
