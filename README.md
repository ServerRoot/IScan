# IScan使用说明

#### 安装模块：

```
pip -r install requirements.txt
```



#### 参数说明

```
-f FILE, --file FILE  指定扫描文件
-o OUTFILE, --outfile OUTFILE 导出文件
-t T                  指定线程数,默认10
-d DIC, --Dic DIC     指定字典文件,默认dict.txt
-size SIZE            指定文件字节大小,默认3500000(用于过滤误报)
```



#### 运行结果

单域名扫描:

python IScan.py --target http://baidu.com

批量扫描:

python IScan.py --targets 指定扫描文件.txt

指定过滤扫描文件大小

python IScan.py --targets 指定扫描文件.txt --size 3500000

指定线程数

python IScan.py --targets 指定扫描文件.txt  -t 50

字典可自行更改

*domain\*关键字可以将域名用于测试泄露的文件名进行测试,文件后缀可自定义

url.txt(待扫描文件)里域名后不能有文件路径







