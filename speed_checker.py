import time
import requests
from datetime import datetime

url = "https://showdeerocks.com/data"

start_time = time.time()
response = requests.get(url)
end_time = time.time()

elapsed_time = end_time - start_time
measurement_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(f"응답까지 걸린 시간: {elapsed_time:.2f}초")

with open("response_time.txt", "a") as f:
    f.write(f"{measurement_time}에 측정한 서버 반응속도 : {elapsed_time}\n")
