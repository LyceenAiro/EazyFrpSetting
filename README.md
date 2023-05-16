# EazyFrpSetting
dev分支现在为version-3版本的准备分支,未来将移动至master 
## 特性
快速批量管理Frp隧道的[客户端](https://github.com/LyceenAiro/EazyFrpSetting)  
## 使用
需要使用该软件配置Frp首先你需要[Frp](https://github.com/fatedier/frp)的软件本体  
- 需求文件:frpc.exe  
- 将frpc.exe放入根目录中
- 启动该软件
### 文件目录生成和排版
```
.
├─data          // 这个文件夹及其内容都是自动生成的
│  ├─frpc.ini       // frpc启动文件
│  ├─link.ini       // link编译文件
│  ├─linktable.ini  // link表源文件
│  ├─more.ini       // other配置文件
│  └─server.ini     // server配置文件
├─frpc.exe      // 你需要把frpc.exe放在这里
└─main.exe      // 软件本体
```
## 开发流程
- [x] 最初开发库构建
- [x] 图形化界面
- [x] 完全重构代码(功能支持)
- [ ] 开发者工具
- [ ] version-3发布
- [x] 界面美化
### 功能支持[最初]
- [x] 修改服务器配置
- [x] 添加链接
- [x] 启动功能
- [x] 输入纠错
- [x] 隧道管理
- [x] 其他功能
- [x] 自述页面
- [x] 托盘图标
- [x] 更新检查
- [x] 重置功能
### 未来功能[计划]
- [ ] 链接开关
未来更多...

## 开发者工具
### ui文件一键编译
使用[ui_install.bat](./ui_install.bat)
- [ ] 日志
### ui文件&qrc文件自动编译
保持打开[auto_ui_install.bat](./auto_ui_install.bat)
默认配置下5秒钟会自动更新一次编译
- [x] 日志 -> auto_ui_install.txt
### 发布文件一键编译(测试)
- 使用[main_install.bat](./main_install.bat)
- [x] 编译
- [ ] 日志
- [ ] _打包_(暂无应用场景)
### 项目main需要的第三方库与文件
(upx)[https://github.com/upx/upx]
```
import PySide6
import qdarkstyle
import requests
```
## LICENSE
[MIT License](./LICENSE)