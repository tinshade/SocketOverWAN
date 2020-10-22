import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
# From tcp:\\2.tcp.ngrok.io:101010Like 2.tcp.ngrok.io and 101010 are URL and PORT respectively!


server_address = ('<NGROK TCP URL>', <NGROK TCP PORT>)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:

    # Send data
    # Message must be converted into bytes before sending.
    message = b'Your Message' #This can be changed to input with an infinite while loop for chatting
    print('Sending...')
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('Sent')

finally:
    print('Dropping the connection')
    sock.close()