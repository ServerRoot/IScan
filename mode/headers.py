import requests
import urllib3
from fake_useragent import UserAgent

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ua = UserAgent()

def get_response(url):
    headers = {'User-Agent': ua.random}
    try:
        proxies = {"http": None, "https": None}
        response = requests.get(url, headers=headers,timeout=5,stream=True, proxies=proxies)
        return response
    except Exception as e:
        # 可以根据需要打印异常信息或进行其他处理
        pass

def get_file_size(response):
    try:
        content_length = response.headers.get("Content-Length")
        if content_length:
            return int(content_length)
    except Exception as e:
        pass
    return None

def get_status_code(response):
    try:
        return response.status_code
    except Exception as e:
        pass
    return None

def get_service_name(response):
    try:
        server_name = response.headers.get("Server")
        return server_name
    except Exception as e:
        pass
    return None

def get_file_type(response):
    try:
        file_type = response.headers.get("Content-Type")
        return file_type
    except Exception as e:
        pass
    return None
