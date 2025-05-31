import pyshark

# Mở file pcapng
cap = pyshark.FileCapture('login_capture.pcapng')

# Duyệt các gói và in thông tin tầng 2 và tầng 3
for pkt in cap:
    try:
        # Tầng 2: Ethernet
        eth_src = pkt.eth.src
        eth_dst = pkt.eth.dst
        # Tầng 3: IP
        ip_src = pkt.ip.src
        ip_dst = pkt.ip.dst

        print(f"[+] Ethernet: {eth_src} --> {eth_dst}")
        print(f"    IP: {ip_src} --> {ip_dst}\n")

    except AttributeError:
        continue  # Bỏ qua gói không có Ethernet/IP
