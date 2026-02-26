# 📱 Telegram 转发回复机器人

一个简单强大的 Telegram 机器人，可以接收用户消息并转发给你，你可以直接在 Telegram 中回复用户消息。

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

## ✨ 功能特性

### 核心功能
- 🔄 **自动转发** - 自动转发所有用户消息给管理员
- 💬 **直接回复** - 支持直接回复用户消息
- 📱 **基于API** - 完全基于 Telegram Bot API
- 🚀 **轻量级** - 无需数据库，开箱即用

### 优势
- ✅ 无需数据库，纯 Python 实现
- ✅ 无需复杂配置，开箱即用
- ✅ 代码简洁易维护，易于扩展
- ✅ 支持多个用户同时对话
- ✅ 完整的日志记录

## 📋 快速开始

### 前置要求

- Python 3.8 或更高版本
- Telegram 账号
- Linux / Windows / Mac 服务器（或本地运行）

### 1️⃣ 获取 Bot Token

1. 打开 Telegram，搜索 `@BotFather`
2. 发送命令 `/newbot`
3. 按照提示输入机器人名称和用户名
4. 复制生成的 Token

**Token 格式示例：**
```
123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefg
```

### 2️⃣ 获取你的 User ID

1. Telegram 搜索 `@userinfobot`
2. 点击 START
3. 机器人会显示你的 User ID（例如：123456789）

### 3️⃣ 克隆项目

```bash
git clone https://github.com/yufengduxing/Bidirectional-Telegram-Bot.git
cd Bidirectional-Telegram-Bot
```

### 4️⃣ 配置

编辑 `tg_bot.py`，修改第 14-15 行：

```python
nano tg_bot.py

ADMIN_ID = 123456789                                                           # 例如: 123456789
BOT_TOKEN = "123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefg"                      # 例如: 123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefg
```

### 5️⃣ 安装依赖

```bash
pip install -r requirements.txt
```

### 6️⃣ 运行

```bash
python3 tg_bot.py
```

看到以下输出说明启动成功：
```
🤖 机器人启动...
```

## 🚀 部署到服务器

### 方案 A：使用 systemd（推荐）

1. **创建服务文件：**

```bash
sudo nano /etc/systemd/system/tg-bot.service
```

2. **填入以下内容（修改路径）：**

```ini
[Unit]
Description=Telegram Forward Bot
After=network.target

[Service]
Type=simple
User=www
WorkingDirectory=/www/wwwroot/telegram-bot
ExecStart=/usr/bin/python3 /www/wwwroot/telegram-bot/tg_bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

3. **启动服务：**

```bash
sudo systemctl daemon-reload
sudo systemctl start tg-bot
sudo systemctl enable tg-bot
```

4. **查看状态：**

```bash
sudo systemctl status tg-bot
```

5. **查看日志：**

```bash
sudo journalctl -u tg-bot -f
```

### 方案 B：使用 nohup（简单方式）

```bash
nohup python3 tg_bot.py > tg_bot.log 2>&1 &
```

**查看日志：**
```bash
tail -f tg_bot.log
```

**停止机器人：**
```bash
pkill -f "python3 tg_bot.py"
```

## 📖 使用说明

### 👥 用户端

1. 搜索你的机器人用户名
2. 点击 START 或发送 `/start`
3. 发送任何消息
4. ✅ 机器人会自动转发给你

### 👨‍💼 管理员端（你）

**接收消息流程：**
```
用户发消息 → 机器人转发 → 你收到
```

**回复用户流程：**
1. 机器人会把用户消息转发给你（格式：`📨 新消息 👤 用户名 (ID) 💬 消息内容`）
2. **长按** 要回复的消息
3. 点击 **回复**
4. 输入你的回复内容
5. 发送 ✅ 用户会自动收到你的消息

## 📁 文件结构

```
telegram-forward-bot/
├── tg_bot.py              # 主程序文件
├── requirements.txt       # Python 依赖列表
├── README.md             # 项目文档（本文件）
├── LICENSE               # MIT 开源协议
├── .gitignore           # Git 忽略文件
└── tg_bot.log           # 日志文件（运行时生成）
```

## ⚙️ 配置说明

### 主配置文件：`tg_bot.py`

**第 14-15 行 - 必须修改：**

```python
ADMIN_ID = 123456789  # 你的 Telegram User ID
BOT_TOKEN = "123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefg"  # 你的 Bot Token
```

**日志配置 - 可选修改：**

```python
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,  # 可改为 logging.DEBUG 获取更详细的日志
    handlers=[
        logging.FileHandler('tg_bot.log'),     # 日志文件名
        logging.StreamHandler()                # 控制台输出
    ]
)
```

## 🔍 故障排除

### ❌ 问题 1：机器人无法启动

**检查步骤：**

1. 检查 Python 版本（需要 3.8+）：
```bash
python3 --version
```

2. 检查依赖是否安装：
```bash
pip list | grep python-telegram-bot
```

3. 验证 Token 和 ID 是否正确：
```bash
grep -E "ADMIN_ID|BOT_TOKEN" tg_bot.py
```

4. 查看错误日志：
```bash
cat tg_bot.log
```

### ❌ 问题 2：用户消息未被转发

**检查步骤：**

1. 查看日志文件：
```bash
tail -n 50 tg_bot.log
```

2. 确认 ADMIN_ID 正确：
```bash
python3 -c "print('Your ID:', 7358821097)"  # 改成你的ID
```

3. 测试网络连接：
```bash
ping api.telegram.org
```

### ❌ 问题 3：回复消息无法发送给用户

**检查步骤：**

1. 确保长按的是转发的消息（必须包含用户ID）
2. 检查错误日志：
```bash
grep "发送失败" tg_bot.log
```

3. 确认网络连接正常

## 🔐 安全建议

⚠️ **重要提示：**

1. **❗ 不要公开你的 Bot Token**
   - Token 是敏感信息，千万不要提交到 GitHub
   - 使用 `.env` 文件或环境变量管理 Token

2. **❗ 不要公开你的 User ID**
   - 在 GitHub 上发布代码前，请修改示例 ID
   - 使用 `.gitignore` 排除配置文件

3. **定期检查日志**
   - 监控异常活动
   - 查看错误信息

4. **限制管理员权限**
   - 只给需要的人设置管理员

### 使用环境变量（推荐方案）

1. **创建 `.env` 文件：**

```bash
echo "ADMIN_ID=你的ID" > .env
echo "BOT_TOKEN=你的Token" >> .env
```

2. **安装 python-dotenv：**

```bash
pip install python-dotenv
```

3. **修改 `tg_bot.py`：**

```python
import os
from dotenv import load_dotenv

load_dotenv()

ADMIN_ID = int(os.getenv('ADMIN_ID'))
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
```

4. **添加到 `.gitignore`：**

```bash
echo ".env" >> .gitignore
```

## 🔧 扩展功能

### 例 1：添加新命令

```python
async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 机器人正在运行中...")

# 在 main() 中添加
app.add_handler(CommandHandler("status", status_command))
```

### 例 2：限制特定用户

```python
ALLOWED_USERS = [123456789, 987654321]

if user.id not in ALLOWED_USERS:
    await update.message.reply_text("❌ 你没有权限使用此机器人")
    return
```

### 例 3：自动回复特定关键词

```python
if "你好" in message_text:
    await update.message.reply_text("你好！很高兴见到你 😊")
    return
```

## 📊 日志说明

机器人会记录所有操作到 `tg_bot.log`：

```
2026-02-23 18:39:01 - INFO - 用户 123456789: 你好
2026-02-23 18:39:02 - INFO - 回复给用户 123456789: 你好！
2026-02-23 18:39:03 - ERROR - 发送失败: Chat not found
```

**查看日志：**
```bash
tail -f tg_bot.log           # 实时查看
tail -n 100 tg_bot.log       # 查看最后 100 行
grep "ERROR" tg_bot.log      # 只看错误信息
```

## 📈 性能优化

对于高流量场景：

1. **使用进程管理器（Supervisor）**：
```bash
sudo apt install supervisor
# 配置 supervisor 配置文件
```

2. **使用 systemd 的多进程配置**：
```ini
[Service]
ExecStart=/usr/bin/python3 -m gunicorn tg_bot:app
```

3. **监控资源使用**：
```bash
ps aux | grep tg_bot.py
top -p $(pgrep -f tg_bot.py)
```
##

### 🤝 贡献指南

欢迎提交 Pull Request！

1. Fork 本项目
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的改动 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request

##

### 📝 许可证

本项目采用 MIT License - 详见 [LICENSE](LICENSE) 文件

### 机场推荐：
- 曙光云：https://dawnscloud.com
- 超实惠：https://cshjc.net

##

### VPS推荐：
- OCI：https://oci.ee

##

### 发卡网：

- 卡链云：https://marts.cc

##

### 📞 联系方式

- TG群组：https://t.me/yufeng_duxing
- 定制联系：https://t.me/martsccbot
- 博客：https://yufengduxing.xyz/
- Github：https://github.com/yufengduxing

##

## ⭐ 致谢

感谢所有使用和支持本项目的人！

## 📚 更新日志

### v1.0.0 (2026-02-23)
- ✨ 初始版本发布
- 🔄 支持消息转发
- 💬 支持直接回复
- 📝 完整文档

---

**⭐ 如果这个项目对你有帮助，请给个 Star！**

