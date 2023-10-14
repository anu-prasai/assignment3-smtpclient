from socket import *
from datetime import datetime
#to test locally use python -m aiosmtpd -n -d; will use localhost and port 8025; documentation at https://aiosmtpd.readthedocs.io/en/latest/manpage.html
def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"
    fromsg='anuprasai1@gmail.com'
    tomsg= 'anuprasai4@gmail.com'
    server=(mailserver, port)
    clientSocket = socket(AF_INET,SOCK_STREAM)
    clientSocket.connect(server)

    recv= clientSocket.recv(1024).decode()

    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    if recv1[:3] != '250':
            print('250 reply not received from server.')

    MailFrom = 'MAIL FROM:<anuprasai1@gmail.com>\r\n'
    clientSocket.send(MailFrom.encode())
    recv2 = clientSocket.recv(1024).decode()
    #print(recv2)
    if recv2[:3] != '250':
            print('250 reply not received from server.')
    # Send MAIL FROM command and handle server response.
    # Fill in start
    # Fill in end
    ecpt="RCPT TO: <anuprasai1@gmail.com> \r\n"
    clientSocket.send(ecpt.encode())
    recv3 = clientSocket.recv(1024).decode()
    #print(recv3)
    if recv3[:3] != '250':
        print('250 reply not received from server.')


    #print("hello")
    data= 'DATA\r\n'
    clientSocket.send(data.encode())
    recv4= clientSocket.recv(1024).decode()
    #print(recv4)
    if recv4[:3] =='354':
        nowtime = datetime.now()
        dt_string = nowtime.strftime("%d/%m/%Y %H:%M:%S")
        clientSocket.send(dt_string.encode())
        clientSocket.send(fromsg.encode())
        clientSocket.send(tomsg.encode())
        clientSocket.send(msg.encode())
        clientSocket.send(endmsg.encode())
        recv6 = clientSocket.recv(1024).decode()
        if recv6[:3] != '250':
            print('250 reply not received from server.')
    else:
        print('354 reply not received from server.')
    # Send DATA command and handle server response.
    # Fill in start
    # Fill in end

    # Send message data.
    # Fill in start
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    # Fill in end
    #print("hello")
    quitnow= 'QUIT\r\n'
    clientSocket.send(quitnow.encode())
    recv5= clientSocket.recv(1024).decode()
    #print(recv5)
    if recv5[:3] == '221':
        #print("221 recvieved")
        clientSocket.close()
    # Send QUIT command and handle server response.
    # Fill in start
    # Fill in end

    #clientSocket.close()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')