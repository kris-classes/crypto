# Week 4 Homework

## Only change the lines beneath TODO: comments.

### 0 - Instructions:

If you haven't already, run `pip install cryptography` and `pip install fire`, two libraries we'll be using during this course.

For homework you'll make `generate_key()`, `encrypt(message)`, and `decrypt(key, ciphertext)` work
by using other functions in the file.

Contact me immediately if you have errors or difficulty getting past this stage.

### 1 - Test the base64_encode function and learn what it does.

Go down to PyCharm's `Terminal` tab and type these commands there. You'll be using it for the rest of the homework.

Run the command `python main.py base64_encode "hello from kris"` and see what
it does.
The program should print: `b'aGVsbG8gZnJvbSBrcmlz'` (remember that the `b`
means this is a string of bytes)

### 2 - Test the base64_decode function and learn what it does.

Run the command `python main.py base64_decode
"QmFzZTY0IGVuY29kaW5nIGlzIE5PVCBlbmNyeXB0aW9uLg=="` and see what it
does.

It should decode to the string `b'Base64 encoding is NOT encryption.'`

### 3 - Test the message_to_bytes function and learn what it does.

This function converts your message to bytes and also adds padding, which is
required for a block-cipher if your message isn't long enough.

Run `python main.py message_to_bytes "hello world"` and you should get the
output:
```shell
Unpadded message: hello world
Padded data: b'hello world\x05\x05\x05\x05\x05'
b'hello world\x05\x05\x05\x05\x05
```


### 4 - Test the remove_pkcs7_padding function and learn how it works.

Run `python main.py remove_pkcs7_padding "hello world\x05\x05\x05\x05\x05"`

You should get the output:

```shell
Removing padding: hello world\x05\x05\x05\x05\x05
padded_data as bytes: b'hello world\\x05\\x05\\x05\\x05\\x05'
Removing PKCS7 padding for: b'hello world\x05\x05\x05\x05\x05'
Data without padding: b'hello world'
b'hello world'
```


### 5 - Make the generate_key function work.

Now that you know how those 4 functions work, run the command: `python main.py
generate_key`. You should get the output: `Your 128-bit key as bytes is: b'
..some random data as bytes...` once it's working.


### 6 - Make the encrypt function work.

Run the command `python main.py encrypt "testing encryption"`.


Once you've made it work you should get output similar (but different because
of the random key) to the following:
```shell
Plaintext message to encrypt is: testing encryption
Generating a key:
Your 128-bit key as bytes is: b'\x8c\xb1\xa2\xbdYw\x12\x10B\xa8\xa0[AJ\x96X'
Key: b'\x8c\xb1\xa2\xbdYw\x12\x10B\xa8\xa0[AJ\x96X'
Base64 encoded key: b'jLGivVl3EhBCqKBbQUqWWA=='
Unpadded message: testing encryption
Padded message: b'testing encryption\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e'
Ciphertext: b'7\x0f\xf5\xc0\xc6L\xdd\x02\x1f]\xd2\xce\xcbl\xe1\xf6\xe5p\x07J\x9b\x9arf\x82RI\xd7\x8e+\x1b\xed'
Base64 encoded ciphertext: b'Nw/1wMZM3QIfXdLOy2zh9uVwB0qbmnJmglJJ144rG+0='
```

Save the `key` and `ciphertext` somewhere (REMOVE the `b` at the start).


### 7 - Make the decrypt function work.

If your ciphertext was `b'somethingbase64` then make sure you remove the `b`
at the start. Run the command `python main.py decrypt KEY CIPHERTEXT` but
replace `KEY` and `CIPHERTEXT` with your key and ciphertext from `6`.

If your decrypt function works, congratulations you've now built a program that
uses modern encryption (although it still has a lot of ways to be attacked!).


### 8 - Decrypt a message from me.

Decrypt the following message and send me your solution.
* Now that your `encrypt` and `decrypt` functions work as expected, decrypt the
  following text.

Using the key `OrTH5lv6THAc4fqmMrA2TQ==`, decrypt the following ciphertext
(triple-click to select the text):

```shell
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
```



### 9 - Encrypt and send me a custom message.

After decrypting 8), encrypt the message "Hello from Firstname-IDNumber. The answer is: {ANSWER}." (replace Firstname and IDNumber with your first name and student ID number, and ANSWER with the answer from 8).

* Save the `key` and `ciphertext` and send them to me with the title 'Week
  4 Homework Solution'.


### 10 - Congratulations, you're done!

