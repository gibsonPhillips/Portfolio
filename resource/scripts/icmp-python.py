from socket import *
import os
import sys
import struct
import time
import select
import binascii  


ICMP_ECHO_REQUEST = 8

def checksum(str): 
	csum = 0
	countTo = (len(str) / 2) * 2
	# does this risk floating point errors? I don't care enough to check, but maybe change to //
	
	count = 0
	while count < countTo:
		thisVal = ord(str[count+1:count+2]) * 256 + ord(str[count:count+1])
		csum = csum + thisVal 
		csum = csum & 0xffffffff  
		count = count + 2
	
	if countTo < len(str):
		csum = csum + ord(str[-1])
		csum = csum & 0xffffffff
	
	#Fill in start
	#add the upper 16 bits with the lower 16bits of csum;
	#add the carry-over bit back to lower bits of csum;
	#flip everybit of csum and put it into variable "answer"
	csum = (csum >> 16) + (csum & 0xffff)
	csum = csum + (csum >> 16)
	answer = ~csum
    #Fill in end
	
	answer = answer & 0xffff 
	answer = answer >> 8 | (answer << 8 & 0xff00)
	return answer 
	
def receiveOnePing(mySocket, ID, timeout, destAddr):
	timeLeft = timeout
	
	while 1: 
		startedSelect = time.time()
		whatReady = select.select([mySocket], [], [], timeLeft)
		howLongInSelect = (time.time() - startedSelect)
		if whatReady[0] == []: # Timeout
			return "Request timed out."
		
		#Fill in start
		# get the time the packet is received and store it in "timeReceived"
		# receive the packet from socket and extract information into "recPacket, addr"
        		# fetch the ICMP header from the IP packet
		# get TTL, icmpType, code, checksum, packetID, and sequence
		# get data payload, and return information that can be print later, including byte_data, time used from packet sent to received, TTL
		timeReceived = time.time()
		recPacket, addr = mySocket.recvfrom(1024)
		icmpHeader = recPacket[20:28]
		type,code,checksum_recv,packetID,sequence = struct.unpack("bbHHh", icmpHeader)

		if packetID == ID:
			bytesInDouble = struct.calcsize("d")
			timeSent = struct.unpack("d", recPacket[28:28 + bytesInDouble])[0]
			rtt = (timeReceived - timeSent) * 1000
			ttl = struct.unpack("B", recPacket[8:9])[0]
			return f"Reply from {destAddr}: bytes = {len(recPacket)} time = {round(rtt, 2)} TTL = {ttl}"
      		#Fill in end
				
		timeLeft = timeLeft - howLongInSelect
		if timeLeft <= 0:
			return "Request timed out. 2"
	
def sendOnePing(mySocket, destAddr, ID):
	# Header is type (8), code (8), checksum (16), id (16), sequence (16)
	
	myChecksum = 0
	# Make a dummy header with a 0 checksum
	# struct -- Interpret strings as packed binary data
	header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
	
	#Fill in start   
	# Use current time as data payload and put it into "data" variable
	# Calculate the checksum on the data and the dummy header and put it into "myChecksum" variable

	data = struct.pack("d", time.time())
	myChecksum = checksum(header + data)
	#Fill in end
	
	# Get the right checksum, and put in the header
	if sys.platform == 'darwin':
		# Convert 16-bit integers from host to network  byte order
		myChecksum = htons(myChecksum) & 0xffff		
	else:
		myChecksum = htons(myChecksum)
		
	#Fill in start   
	# update the header with correct checksum
	# create a variable "packet" that combines the header and the data payload

	header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
	packet = header + data
	#Fill in end
		
	mySocket.sendto(packet, (destAddr, 1)) # AF_INET address must be tuple, not str
	# Both LISTS and TUPLES consist of a number of objects
	# which can be referenced by their position number within the object.
	
def doOnePing(destAddr, timeout): 
	icmp = getprotobyname("icmp")
	
	#Fill in start   
	# create a socket with SOCK_RAW as the socket type, and icmp as the protocol; 
	# SOCK_RAW is a powerful socket type. For more details:   http://sock-raw.org/papers/sock_raw
	mySocket = socket(AF_INET, SOCK_RAW, icmp)
	#Fill in end
	
	myID = os.getpid() & 0xFFFF  # Return the current process i
	sendOnePing(mySocket, destAddr, myID)
	delay = receiveOnePing(mySocket, myID, timeout, destAddr)
	
	mySocket.close()
	return delay
	
def ping(host, timeout=1, count=4):
    dest = gethostbyname(host)
    print(f"Pinging {dest} using Python:")
    print("")

    rtts = []
    for i in range(count):
        delay = doOnePing(dest, timeout)
        print(f"delay: {delay}")
        if "time =" in delay:	
			try:
				time_ms = float(delay.split("time =")[1].split("ms")[0])
				rtts.append(time_ms)
            except: print("failed to parse RTT")
        time.sleep(1)

    if rtts:
        print(f"\n--- {host} ping statistics ---")
        print(f"{count} packets transmitted, {len(rtts)} received, {round((1 - len(rtts)/count)*100)}% packet loss")
        print(f"rtt min/avg/max = {min(rtts):.2f}/{sum(rtts)/len(rtts):.2f}/{max(rtts):.2f} ms")
    else:
        print("All requests timed out.")

# def ping(host, timeout=1):
# 	# timeout=1 means: If one second goes by without a reply from the server,
# 	# the client assumes that either the client's ping or the server's pong islost
# 	dest = gethostbyname(host)
# 	print("Pinging " + dest + " using Python:")
# 	#print "Pinging " + dest + " using Python:"
# 	print("")
# 	#print ""
# 	# Send ping requests to a server separated by approximately one second
# 	while 1 :
# 		delay = doOnePing(dest, timeout)
# 		print(delay)
# 		time.sleep(1)# one second
# 	return delay
	
ping("google.com")

