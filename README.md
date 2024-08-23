# LAN-Chat-Server
simple chat server for LAN, The Chat server will brodcast massage to all client
---
## How it work

1. Client will send a massage to a server and the server will brodcast the massage to all connected client
    - each client will have their own thread in the server for receiving message for each client
    - Client will thread between recving massage and sending massage
---
