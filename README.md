# EazyFrpSetting
- 快速使用图形化来管理Frp隧道的客户端  
- 程序中快速关闭调试Frp
- 将程序最小化至托盘运行
- 支持多隧道图形化管理
- 隧道自动生成部分信息
- 检测带宽状态自动预警
- 检测Frp服务器状态
## 界面
- 使用`PySide6`编写
- 部分美化`qdarkstyle`  
![Example Image](https://raw.githubusercontent.com/LyceenAiro/EazyFrpSetting/doc/v3_file/show_file/2.png)
## 使用
该软件基于frp_0.57.0_windows_xx版本开发  
适用于原版frps自建的服务器，未来有可能兼容其他分支的frp  
需要使用该软件配置Frp首先你需要[Frp](https://github.com/fatedier/frp)的软件本体  
- 需求文件`frpc.exe`  
- 将`frpc.exe`放入根目录中
- 启动该软件
- 2.1.0版本以后只支持使用toml作为配置的frpc版本
### 文件目录生成和排版
```
.
├─data          // 这个文件夹及其内容都是自动生成的
│  ├─frpc.toml       // frpc启动文件，你可以在编译完成后手动编辑它
│  ├─link.toml       // link编译文件，在表源文件更新后软件的编译器会将其编译成frpc格式
│  ├─linktable.toml  // link表源文件，在此处存储`配置链接`页面中的各项属性
│  ├─more.ini       // other配置文件，版本变动可能会让它失效，初始化后旧文件会备份
│  └─server.toml     // server配置文件，存放了服务器的基本配置
├─frpc.exe      // 你需要把frpc.exe放在这里，当然不放也可以启动软件
└─client.exe      // 软件本体
```
## 开发流程
- [x] 最初开发库构建
- [x] 图形化界面
- [x] 完全重构代码(功能支持)
- [x] 界面美化
- [x] 开发者工具
- [x] version-3发布
### 未来功能[计划]
- [x] 链接开关 v2.1.3优化
- [x] 链接功能
- [x] 重构配置接口(toml重构)
- [x] 检测服务
- [x] 流量监视
- [x] 修复链接功能(toml重构)
- [x] log日志关键词翻译 v2.2.0
- v3代码架构难以维护，已经不能承载更多功能，后续只会修复问题和体验优化
- 如果未来有机会，将在v4重构后推出更多功能
## 开发者工具
### ui文件&qrc文件自动编译
- 保持打开[auto_ui_install.bat](./auto_ui_install.bat)  
- 默认配置下5秒钟会自动更新一次编译
- bug: 编译后main_ui的import main_rc需要手动修改为import ui.main_rc
### 发布文件一键编译
- 使用`python`运行[main_install.py](./main_install.py)
- [x] 编译
- [x] 打包
### 编译main需要的程序与第三方库
安装[python3.8+](https://www.python.org/)  
下载[upx](https://github.com/upx/upx),将其文件夹解压到库根目录,修改`main_install.py`以下参数`可选`
``` python
upx = "upx文件夹名称"
```
使用`pip`安装`编译环境`
``` cmd
pip install -r requirements.txt
```
## LICENSE
[MIT License](./LICENSE)