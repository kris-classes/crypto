# HTCS6702 Week 5 Homework

## Exercise 0 - Basic usage of threads for concurrency.

Make sure you still have the `fire` library installed from Week 4. If you don't then run `pip
install fire`.
NOTE: Use the `python3` command on Kali linux. The `python` command runs version 2.7 (the old unsupported one) and some commands won't work.
You don't need to do any coding for this example, but try to understand what the
code is doing. Watch this video on using PyCharm's Debugger for how to use this
feature: https://www.youtube.com/watch?v=sRGpvbhOhQs

1. First run `python threading_example.py slow_function` then go and look at
   the code. It's using `time.sleep(5)` which just tells Python to sleep for
   5 seconds. This simulates what happens when you make a network or large file
   request in a programming language.

2. Run `python threading_example.py slow_functions_without_threads`. This runs
   slow_function 4 times without using threads. Threads allow us to use
   concurrency, which is another name for multitasking. Without using threads,
   all of our code runs sequentially, or one after the other. Each time we call
   slow_function() in the for-loop, we have to wait another 5 seconds.

3. Run `python threading_example slow_functions_with_four_threads`. This runs
   slow_function 4 times but uses threads. The code is a tiny bit more complex,
   but all of the functions run concurrently, so all 4 of them take 5 seconds
   to run. All of you have multicore CPUs, with each core having 2 hardware
   threads. Hardware threads behave differently to software threads (which is
   what we're using in our code), but both enable concurrency.


4. What happens if our computer only has 2 cores and 4 threads, or 4 cores and
   8 threads? What if we try to run 50 threads? Will Python run 8 at a time,
   then run another 8 in 5 seconds, and so on?

   Run `python threading_example.py slow_functions_with_forty_threads`.

   How long does it take to finish? This is because Python's `sleep()` function
   tells the operating system to go and do something else while it waits. The
   OS is always switching between different processes and threads.

5. Try and create your own function using some basics you've learned so far and
   use the examples to test and understand how threads behave. Remember to use
   PyCharm's built-in debugger functionality.


## Exercise 1 - Using netcat as a client.

Either open Kali in a VM, or install `netcat` on your operating system. Netcat
(aka `nc`) can be used as a client to talk to services. It opens a socket and
connects to whatever you want. **NOTE: Kali's netcat version may have different command arguments to other versions. Contact me if a command doesn't work**.

* HTTP request with netcat

Open a terminal and type `nc ifconfig.me 80`. This connects to the website
http://ifconfig.me

Type the following and then **press ENTER twice (2x)**:
```shell
GET / HTTP/1.1
Host: ifconfig.me


```

You should receive a response containing HTTP headers and your IP address. This
is how web browsers work. Try it with a few other websites like youtube.com, google.com, netflix.com etc.
You'll notice that you keep receiving HTTP 301 - Moved Permanently. This is because most sites these days redirect users from HTTP (insecure) to HTTPS (secure). Unfortunately netcat doesn't support HTTPS by default, but we can use `openssl` to see how an HTTPS connection looks. Unlike HTTP running on `port 80`, HTTPS uses `port 443` so we have to connect to that instead.

```shell
openssl s_client -connect youtube.com:443

# Lots of HTTPS (TLS) certificate information will appear. We'll learn more about this later in the course.
GET / HTTP/1.1


# press Enter twice
```

Notice that sometimes you get `HTTP/1.1 400 Bad Request`. We can talk more about this later in the course when we learn about HTTP and TLS.
Now you know how your web browser communicates with websites! Cool huh?!


## Exercise 2 - Using netcat as a server.

Run `nc -l -p 1234` in a terminal window then open your **Kali web browser** and connect to
[http://localhost:1234](http://localhost:1234). **Your browser will be 'Loading' forever**, so switch to the netcat window and it will display your
browsers HTTP request in its console, which looks something like this:

```shell
GET / HTTP/1.1
Host: localhost:1234
Connection: keep-alive
... blah blah etc etc
```

Before your browser request times out, type this into the netcat terminal and check your browser after typing each line:

```shell
HTTP/1.1 200 OK

<b>hello</b>
<p>this is a test</p>
<h1>blah blah blah</h1>
```

`Press Ctrl-C to close the netcat server`.

Your browser thinks that it's connecting over a really slow internet connection, and
technically it is. This is essentially how web browsers and web servers work.


## Exercise 3 - Using netcat as both a client and server.

Create a netcat server with `nc -l -p 1234` in one terminal window.
Open another terminal window and connect to the server with `nc localhost
1234`. Type commands into each window and watch as the output appears in the other window. You can do this for both the server and the client. This is how sockets and network applications work. Use `Ctrl-C` to
close netcat in each terminal window.

## Exercise 4 - Viewing bytes sent with netcat.

Netcat supports `hexdump` mode with the `-x` argument.
Run the server with `nc -x -l -p 1234` then connect to it again in a different
terminal window with `nc localhost 1234`. Start typing things and watch as data
appears in the server terminal. You should see something like this:

```shell
hello
Received 6 bytes from the socket
00000000  68 65 6C 6C  6F 0A                                  hello.
how are you
Received 12 bytes from the socket
00000000  68 6F 77 20  61 72 65 20  79 6F 75 0A               how are you.
```

## Exercise 5 - Reverse shell with netcat.

Netcat allows you to run any command you like on the server.
Run the command `nc -l -p 1234 -e whoami` in a terminal window (you may need to instead run `nc -l -p 1234 -c whoami` on Kali Linux if you get `exec whoami failed`), then connect to
it with `nc localhost 1234` in another terminal window.

What happens if you replace `whoami` with the command `ls -al`? What about the
command `id`? What about if you use the command `$SHELL` and start typing in
things like `ls -al` or `whoami` after connecting with the client? This is
a reverse shell.


## Exercise 6 - Using Socket Programming and Python to talk to a netcat server.

Run `nc -x -l -p 1234` then open a Python shell/console.

Type the following into Python to create a client socket:
```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 1234))
s.send(b'hello')
```

You should see data being sent to netcat. If you pay close attention you'll see
that Python isn't sending a newline character. Try send one and see how the
netcat output changes.

```python
s.send(b'hello\n')
```

We can also send data from netcat back to the Python socket.
Type `hello from the server` into the netcat window. Nothing happens in Python?
Python has received it, but it's sitting in a buffer waiting to be read by the
programmer (you). Type the following into Python.

```python
s.recv(50)
```

This tells Python to try and receive 50 bytes of data from the buffer. It
receives the data as a bytestring (a string of bytes).

What if we only want to receive 2 bytes at a time? Go back to the netcat server
and type `this is a test from the netcat server.` Then go back to python and
type:

```python
s.recv(3)
s.recv(3)
s.recv(3)
s.recv(3)
s.recv(3)
s.recv(3)
s.recv(50)
```

What happens if we try to receive data and the buffer is empty? Try it! Type
this into Python.

```python
s.recv(50)
```

Nothing happens right? Python is **blocked**, waiting to receive input. Go over
to the netcat server and type `hello!` then press Enter. Python will display
the data as soon as it receives it. This is how we use Python as a client to
talk to netcat.

Close the netcat server and close the Python socket. You need to clean up after
yourself or Python can leave sockets open.

```python
s.close()
```


## Exercise 7 - Talking to a webserver with Python sockets

Let's create a new socket and try to find our public IP address using Python.

```python
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('ifconfig.me', 80))
s.send(b'GET / HTTP/1.1\nHost: ifconfig.me\n\n')
```

This sends an HTTP request to `ifconfig.me`. It's exactly the same as what we
did earlier with netcat. The `\n` sends the `newline` `0x0A` (also called `line-feed`) character, equivalent to
pressing `Enter` on the keyboard. HTTP expects two newlines before sending
data. After running this function you'll see the number `34`. This means that
Python sent 34 bytes to the website.

The website sent a response into our sockets buffer. Let's access it by asking
for 500 bytes from the socket buffer.

```python
s.recv(500)
```

We'll see something like

```shell
b'HTTP/1.1 200 OK\r\naccess-control-allow-origin: *\r\ncontent-length: 14\r\ncontent-type: text/
plain; charset=utf-8\r\ndate: Thu, 01 Apr 2021 04:39:15 GMT\r\nx-envoy-upstream-service-time: 5\
r\nVia: 1.1 google\r\n\r\n1.2.3.4'
```

What are the `\r` characters? Some operating systems (Windows) send 2 bytes
when you press `Enter` on the keyboard. The first is `0x0D` or `Carriage
Return`, the 2nd is `0x0A` or `Line Feed`. Unix-based operating systems (Mac
and Linux) just sent `Line Feed`. These different line endings sometimes lead
to problems when sending text between different operating systems, but that
conversation is for another time!

Close the socket.

```python
s.close()
```


## Exercise 8 - Creating a server with Python using sockets

Now we're going to create a server with Python and talk to it using netcat.

```python
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 1234))  # Tells Python what port to use for the server.
s.listen()
```

Now connect up to the socket using netcat and send some data.

```shell
nc localhost 1234
hello from netcat
```

The data has been sent to Python, but Python is waiting for us to accept it.

```python
client_socket, address = s.accept()
```

We've just done something called `tuple-unpacking`. The `s.accept()` command
returns two values. The one we care about is `client_socket`. We can view the
data sent to `client_socket` by running the recv command again.

```python
client_socket.recv(50)  # Ask for 50 bytes of data from the socket buffer
```


We can also send a reply back by running:

```python
client_socket.send(b'response from python!\n')
```

We should see this appear in the netcat window. Let's send another message back
to the server in netcat.

```shell
hello again from netcat
```

Receive the data again with:

```python
client_socket.recv(50)
```

Now you're getting the hang of how client-server communication works. What
happens if we want to have **two** clients talking to the server? Open
a **third** terminal window and connect again using netcat.

```shell
nc localhost 1234
hello from a 2nd netcat client
```

The connection request is sitting with the server, waiting to be accepted.
Let's accept it.

```python
client_socket2, address2 = s.accept()
```

Remember that we've still got some data sitting in the buffer of
`client_socket2`? Receive it!

```python
client_socket2.recv(100)  # This asks for 100 bytes of data
```

If there's less than 100 bytes of data in the buffer (there is) then Python
will just get whatever is in it. We already know what happens when there is
more. How do we send a reply to `client_socket2`? Easy!

```python
client_socket2.send(b'hello to client 2 from the server!\n\n')
client_socket.send(b'hello to client 1 from the server!\n\n')
```

This is essentially how *ALL* TCP-based networking services work. Using UDP sockets
is left as an exercise for you. ;)

Let's clean up after ourselves.

```python
client_socket.close()
client_socket2.close()
s.close()
```


## Exercise 9 - Recreating a simple single-client netcat in Python.


I've created a simple single-client version of netcat in Python. The code is in
`simple_netcat.py`. You can run the server with:

```python
python simple_netcat.py server
```

And run the client in a different terminal window with:

```python
python simple_netcat.py client
```

Take the time to understand how this code works, as you'll be using it for the
assignment.


## Exercise 10 - Computing a checksum.

Python has built-in support for checksums. One of the most common checksums
you'll encounter is called `CRC32`. Google it for more information. In order to generate CRC checksums for data we'll use Python's `zlib` module.

```python
import zlib

zlib.crc32(b'hello')
zlib.crc32(b'blahblah')
zlib.crc32(b'plumless')
zlib.crc32(b'buckeroo')
```

Oops! We got a collision this easily. CRC32 is ok for some things, but not for
us. We need to use hashing.


## Exercise 11 - Hashing

Python has another great builtin library called `hashlib` which has support for
SHA256, SHA3, BLAKE2b, and some other hash functions.

```python
import hashlib

sha2_example = hashlib.sha256(b'hello')
sha3_example = hashlib.sha3_256(b'hello')
blake2b_example = hashlib.blake2b(b'hello')

sha2_example.hexdigest()
sha3_example.hexdigest()
blake2b_example.hexdigest()
```

The `hexdigest()` function shows the output of these hash functions as hex
digests, but we can also see them as bytes.

```python
sha2_example.digest()
sha3_example.digest()
blake2b_example.digest()
```

We usually want them as bytes if we're going to send them over a network.


## Exercise 12 - Message Authentication Codes (and Integrity)

For this final exercise we're going to use a cipher-based message
authentication code, also known as a CMAC. Open the documentation at
[https://cryptography.io/en/latest/hazmat/primitives/mac/cmac.html](https://cryptography.io/en/latest/hazmat/primitives/mac/cmac.html).

```python
from cryptography.hazmat.primitives import cmac
from cryptography.hazmat.primitives.ciphers import algorithms
import os

key = os.urandom(16)  # generate a 16-byte (128-bit) key
print(f'Save this key somewhere: {key}')
c = cmac.CMAC(algorithms.AES(key))
message = b'attack at dawn')
c.update(message)
mac_to_send = c.finalize()
print(f'The MAC to send is: {mac_to_send}')
```

We're not encrypting the message `hello` here, we're just generating a MAC for
it, which allows us to cryptographically check if the message has been changed in transit.
Pretend that we then send the MAC (unencrypted) across the network, along
side the **unencrypted 'attack at dawn' message**. Using it with an unencrypted
message is obviously something we'd **NEVER** want to do, but it simplifies this example to show how MACs are used for integrity. We'll combine them with encryption later in the course.

Now open another terminal window and imagine that you've received the message
'attack at dawn' along with the MAC (the MAC will depend on the key, which we
also keep secret as usual). Open Python in the other terminal window and type:


```python
from cryptography.hazmat.primitives import cmac
from cryptography.hazmat.primitives.ciphers import algorithms

key = WHAT_WAS_THE_KEY_FROM_EARLIER?  # TODO: Replace this with your key from
above.
print('Remember that you need to use the same key from earlier.')
mac_we_received = PUT_THE_MAC_FROM_EARLIER_HERE  # TODO: Replace this with the
MAC from earlier.
print('Remember to use the MAC from earlier')
c = cmac.CMAC(algorithms.AES(key))
message = b'attack at dawn'
c.update(message)  # This regenerates the MAC for the message we received
c.verify(mac_we_received)
```

If nothing happens, then the MAC was valid and it worked. This is how the
`cryptography` library behaves. If our message was modified then Python raises
an `InvalidSignature` exception. Try it.

```python
c = cmac.CMAC(algorithms.AES(key))
message = b'attack at dawn'
some_invalid_mac = b'blahblah'
c.update(message)  # This regenerates the MAC for the message we received
c.verify(some_invalid_mac)

Traceback (most recent call last):
...
cryptography.exceptions.InvalidSignature: Signature did not match digest.
```

This concludes Week 5 homework. Well done! Practice everything here and reach
out if there's a mistake or if something doesn't make sense.

