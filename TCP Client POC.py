
# coding: utf-8

# In[1]:


####################################################
### Creating a TCP CLient using the socket module ##
####################################################
import socket

target_host, target_port = "wwww.google.com", 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

