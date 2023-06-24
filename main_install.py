import os
from makefile.tags import tags

# upx地址
upx = "upx-4.0.2-win64"

# 编译
os.system(f"pyinstaller -F -i ./ui/icon/logo.ico --noconsole --upx-dir={upx} --collect-all charset_normalizer  client.py")

# 输出文件重新命名
outfile = f"./dist/EFS_client_{tags().version}.exe"
if os.path.exists(outfile):
    print("INFO: delete older file")
    os.remove(outfile)
print("INFO: packing rename")
os.rename("./dist/client.exe", outfile)

# 等待查询日志
input("编译完成...")