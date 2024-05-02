import argparse
from mode import file_scan
from concurrent.futures import ThreadPoolExecutor

# 设置全局变量，包括默认请求超时时间和线程数
DEFAULT_THREADS = 10

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", type=str, help="扫描单个目标")
    parser.add_argument("--targets", type=str, help="指定扫描文件")
    parser.add_argument("-o", "--outfile", type=str, default="./result.txt", help="导出文件")
    parser.add_argument("-t", type=int, default=DEFAULT_THREADS, help="指定线程数，默认10")
    parser.add_argument("-D", "--Dic", type=str, default="./dic/dict.txt", help="指定字典文件，默认dict.txt")
    parser.add_argument("-size", type=int, default=3500000, help="指定文件字节大小，默认3500000（用于过滤误报）")
    return parser.parse_args()

def process_url(url, payload_dic, file_size, out_file, pool):
    domain = url.strip("/").replace("https://", "").replace("http://", "")
    with open(payload_dic, "r", encoding="utf-8") as dic:
        for catalogue in dic:
            payload = f"http://{domain}/{catalogue.replace('*domain*', domain).strip()}"
            pool.submit(file_scan.scan_file, payload, file_size, out_file)


def main():
    print('''
           ___            ___                        
          |_ _|    o O O / __|   __    __ _   _ _    
           | |    o      \__ \  / _|  / _` | | ' \   
          |___|  TS__[O] |___/  \__|_ \__,_| |_||_|  
        _|"""""|{======||"""""||"""""||"""""||"""""| 
        "`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"
                                        作者: tutu
    ''')

    args = parse_args()
    payload_dic = args.Dic
    file_size = args.size
    out_file = args.outfile
    task = args.t

    if args.target:
        targets = [args.target]
    elif args.targets:
        with open(args.targets, "r", encoding="utf-8") as urls:
            targets = [url.strip() for url in urls]
    else:
        print("[-] 请指定扫描文件")
        return

    with ThreadPoolExecutor(task) as pool:
        for target in targets:
            print("Url: \t\t\t File-Type: \t\t\t Server-name:")
            future = process_url(target, payload_dic, file_size, out_file, pool)

if __name__ == '__main__':
    main()
