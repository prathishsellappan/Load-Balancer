# Load Balancer Project

This project consists of two simple backend TCP servers and a Python-based load balancer that distributes client requests across the servers.

## 📁 Project Structure

```
backend_server1.py
backend_server2.py
loadbalancer.py
README.md
```

---

## 🚀 Backend Servers

Each backend server listens on a specified port and returns a simple greeting message.

### Running Server 1

```
python backend_server1.py 8888
```

### Running Server 2

```
python backend_server2.py 9999
```

Both servers:

* Accept TCP connections
* Sleep for 1 second (simulating processing delay)
* Send a message: `Hello from server on port <port>!`

---

## ⚖️ Load Balancer

The load balancer listens on port **5555** and forwards client requests to backend servers using either:

* **Random selection**, or
* **Round Robin scheduling**

The provided code uses **Round Robin** by default.

### Features

* Uses `select()` for handling multiple sockets
* Maintains a **flow table** to map client sockets to backend server sockets
* Forwards data in both directions
* Logs connection, message transfer, and disconnection events

### Running the Load Balancer

```
python loadbalancer.py
```

Then connect using `nc` (netcat), telnet, or a custom client:

```
nc localhost 5555
```

Each new connection is forwarded to the next backend server.

---

## 🔄 Flow Summary

1. Client connects to Load Balancer (LB)
2. LB selects backend server (random/round-robin)
3. LB creates server-side socket and connects to backend
4. LB forwards data between client ↔ backend
5. On disconnect, LB closes and removes sockets

---
