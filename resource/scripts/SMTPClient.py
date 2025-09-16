import ssl
import base64
from socket import *

# Email credentials
sender_email = "gcaryp4@gmail.com"
receiver_email = "gcphillips@wpi.edu"
password = ""
#create the App password here:
#https://support.google.com/accounts/answer/185833?visit_id=638759601307026124-2089972828&p=InvalidSecondFactor&rd=1

# Email content, replace with your own message and subject line
msg = "I am computer networks!"    
endmsg = "\r\n.\r\n"
subject = "Greetings computer networks!"

# specify Gmail SMTP server details
mailserver = "smtp.gmail.com"
smtp_port = 587

# Create TCP socket (clientSocket) and establish a connection, and print out the response
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, smtp_port))

recv = clientSocket.recv(1024).decode()
print(recv)

# Secure connection with TLS by sending out Hello message (EHLO for TLS, not HELO) and print out the response
clientSocket.send(b"EHLO user\r\n")
recv1 = clientSocket.recv(1024).decode()
print(f"1: {recv1}")

#initiate a TLS (Transport Layer Security) handshake; STARTTLS command tells the server to start a TLS encryption
clientSocket.send(b"STARTTLS\r\n")
recv2 = clientSocket.recv(1024).decode()
print(f"2: {recv2}")

context = ssl.create_default_context()
clientSocket = context.wrap_socket(clientSocket, server_hostname=mailserver)

# Authenticate
auth_command = "AUTH LOGIN\r\n"
clientSocket.send(auth_command.encode())
recv3 = clientSocket.recv(1024).decode()
print(f"3: {recv3}")

#send out email address for gmail
clientSocket.send(base64.b64encode(sender_email.encode()) + b"\r\n")
recv4 = clientSocket.recv(1024).decode()
print(f"4: {recv4}")

#send out password
clientSocket.send(base64.b64encode(password.encode()) + b"\r\n")
recv5 = clientSocket.recv(1024).decode()
print(f"5: {recv5}")

# Send MAIL FROM command, and print out the response 
clientSocket.send(f"MAIL FROM:<{sender_email}>\r\n".encode())
recv6 = clientSocket.recv(1024).decode()
print(f"6: {recv6}")

# Send RCPT TO command and print out the response 
clientSocket.send(f"RCPT TO:<{receiver_email}>\r\n".encode())
recv7 = clientSocket.recv(1024).decode()
print(f"7: {recv7}")

# Send DATA command and print out the response 
clientSocket.send(f"DATA\r\n".encode())
recv8 = clientSocket.recv(1024).decode()
print(f"8: {recv8}")

# Send email content, including subject, message, and endmsg, and print out the response 
message = f"Subject: {subject}\r\n{msg}\r\n{endmsg}"
clientSocket.send(message.encode())
recv9 = clientSocket.recv(1024).decode()
print(f"9: {recv9}")

# Send QUIT command and print out the response
clientSocket.send(f"QUIT\r\n".encode())
recv10 = clientSocket.recv(1024).decode()
print(f"10: {recv10}")

# Close client socket
clientSocket.close()
print("connection closed")