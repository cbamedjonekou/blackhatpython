
# coding: utf-8

# ### Creating a TCP CLient using the socket module 
# 
# ####  Assumptions:
# 
# * Assumed success in our connection and included no exception handling
# 
# * Assumed the server is always expecting us to send data first. Not always happens in the order.
# 
# * Assumed that the server will always send us data back in a timely fashion. This is not always the case.

# In[1]:


import socket

# We define variables that hold the target host and port number 
# we're going to pull data from.
target_host, target_port = "wwww.google.com", 80

# Then we create our socket object
# socket.socket() is used to create the socket object
# It takes two parameters: AF_INET, and SOCK_STREAM
# The AF_INET parameter is saying we are going to use a standard IPv4 address or hostname
# AF_INET represents the parameter for the socket domain (Address Family-Internet Networking)
# SOCK_STREAM indicates that this will be a TCP client. 
# SOCK_STREAM represents the parameter for the socket type
# Link: https://github.com/python/cpython/blob/3.7/Lib/socket.py
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# After we connect the the socket to a remote address (client.connect(address)).
# For IP sockets, the address is a tuple (host, port).
address = (target_host, target_port)
client.connect(address)


# The following can also be written as such where adding `b` to the front of the string in sentData treats it as a `bytes parameter`:
# 
# ```python
# sentData = b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
# client.send(sentData)
# 
# buffersize = 4096
# response = client.recv(buffersize)
# ```

# In[2]:


# Once we connect we send some data
# Sent Data is in the form of a unicode string
sentData = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
client.send(sentData.encode('utf-8'))


# Then we retrieve the response
buffersize = 4096
response = client.recv(buffersize).decode('utf-8')


# #### Response for sending some data

# In[3]:


print(response)

