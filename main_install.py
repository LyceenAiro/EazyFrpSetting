# version 240428
import os
import sys
from makefile.tags import tags

# upx地址
upx = "upx-4.2.3-win64"

# 编译
os.system(f"pyinstaller -F -i ./ui/icon/logo.ico --noconsole --upx-dir={upx} --collect-all charset_normalizer  client.py")

# 输出文件重新命名
py_version = sys.version.split(' ')[0].split(".")[0]+sys.version.split(' ')[0].split(".")[1]
if tags().versionaddit == "Release":
    outfile = f"./dist/EFS_client_{tags().version}R{py_version}.exe"
elif tags().versionaddit == "alpha":
    outfile = f"./dist/EFS_client_{tags().version}a{py_version}.exe"
elif tags().versionaddit == "beta":
    outfile = f"./dist/EFS_client_{tags().version}b{py_version}.exe"
else:
    outfile = f"./dist/EFS_client_{tags().version}_nocp_{py_version}.exe"
if os.path.exists(outfile):
    print("INFO: delete older file")
    os.remove(outfile)
print("INFO: packing rename")
os.rename("./dist/client.exe", outfile)

# 等待查询日志
input("编译完成...")