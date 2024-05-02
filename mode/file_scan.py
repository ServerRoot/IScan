from . import headers
import requests

def scan_file(url, byte_size, out_file):
    response = headers.get_response(url)
    if response is not None:
        if response.status_code != requests.codes.not_found and headers.get_file_size(response) >= byte_size:
            with open(out_file, "a", encoding="utf-8") as res:
                result = f"{url}\t{headers.get_file_type(response)}\t{headers.get_service_name(response)}"
                print(result)
                res.write(f"{url}\n")
                res.close()