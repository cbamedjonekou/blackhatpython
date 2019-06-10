
# coding: utf-8

# ### Creating a TCP CLient using the socket module 

# In[1]:


import socket

# We define variables that hold the target host and port number 
# we're going to pull data from.
target_host, target_port = "wwww.google.com", 80

# Then we create our socket object
# socket.socket() is used to create the socket object
# It takes two parameters: AF_INET, and SOCK_STREAM
# AF_INET represents the parameter for the socket domain 
# By setting AF_INET (Address Family-Internet Networking) as the socket domain parameter 
# only IP (Internet Protocols) addresses can be used by the socket
# SOCK_STREAM represents the parameter for the socket type
# Link: https://github.com/python/cpython/blob/3.7/Lib/socket.py
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# After we connect the the socket to a remote address (client.connect(address)).
# For IP sockets, the address is a tuple (host, port).
address = (target_host, target_port)
client.connect(address)

