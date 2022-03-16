# Here's some code to get you started, it's a bit verbose,
# but it illustrates a full connection, sending, receiving, and closing the connection.
# You can run it on your dev computer and then use a tool like ncat (nmap's implementation of netcat) to connect,
# i.e.: ncat --sctp localhost 80.


# Here are the packages that we need for our SCTP server
import socket
import sctp
from   sctp import *
import threading

# Let's create a socket:
my_tcp_socket = sctpsocket_tcp(socket.AF_INET)
my_tcp_port   = 80

# Here are a couple of parameters for the server
server_ip     = "0.0.0.0"
backlog_conns = 3

# Let's set up a connection:
my_tcp_socket.events.clear()
my_tcp_socket.bind((server_ip, my_tcp_port))
my_tcp_socket.listen(backlog_conns)

# Here's a method for handling a connection:
def handle_client(client_socket):
  client_socket.send("Howdy! What's your name?\n")
  name = client_socket.recv(1024) # This might be a problem for someone with a reaaallly long name.
  name = name.strip()

  print "His name was Robert Paulson. Er, scratch that. It was {0}.".format(name)
  client_socket.send("Thanks for calling, {0}. Bye, now.".format(name))
  client_socket.close()

# Now, let's handle an actual connection:
while True:
    client, addr   = my_tcp_socket.accept()
    print "Call from {0}:{1}".format(addr[0], addr[1])

    client_handler = threading.Thread(target = handle_client,
                                      args   = (client,))
    client_handler.start()