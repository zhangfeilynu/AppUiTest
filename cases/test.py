
result = b'\tpkg: /data/local/tmp/c_main.apk\r\r\nSuccess\r\r\n'
print(result.decode())
if result.decode().__contains__('Success'):
    print(True)