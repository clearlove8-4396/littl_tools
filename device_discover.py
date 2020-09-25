import socket
import sys
ip = "239.255.255.250"
port = 3702

def getOnvifIp():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # udp
    except socket.error, msg:
        # "Failed to create socket.Error code: " + str(msg[0]) + ", Error messgae: " + msg[1]
        sys.exit()

    # # "Socket Created"

    s.settimeout(5)

    try:
        s.sendto(message, (ip, port))
    except socket.error:
        # "Send failed!"
        sys.exit()

    # # "Message send successfully"

    # 接收返回信息
    l = []

    try:
        while 1:
            data = s.recvfrom(1024)
            # data[0]
            if not data: break
            l.append(data[1])
    except socket.error:
        s.close()
    return l

if __name__ == '__main__':
    print(getOnvifIp())
