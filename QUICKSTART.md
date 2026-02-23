# 🚀 快速开始指南

## 5 分钟内启动机器人

### Step 1: 获取 Token 和 ID（2 分钟）

#### 获取 Bot Token

1. 打开 Telegram，搜索 `@BotFather`
2. 发送 `/newbot`
3. 输入机器人名称（例如：My Forward Bot）
4. 输入用户名（例如：my_forward_bot_2026，必须以 bot 结尾）
5. 复制返回的 Token

**示例 Token：**
```
8540883418:AAEmT-gA9Yw160Jg_mKR-l36Kdp_ESZaPFM
```

#### 获取你的 User ID

1. Telegram 搜索 `@userinfobot`
2. 点击 START
3. 记下显示的 ID

**示例 ID：**
```
7358821097
```

### Step 2: 配置（2 分钟）

打开 `tg_bot.py`，修改第 14-15 行：

```python
ADMIN_ID = 7358821097                                        # 改成你的 ID
BOT_TOKEN = "8540883418:AAEmT-gA9Yw160Jg_mKR-l36Kdp_ESZaPFM"  # 改成你的 Token
```

### Step 3: 安装和运行（1 分钟）

```bash
# 安装依赖
pip install -r requirements.txt

# 运行
python3 tg_bot.py
```

看到 `🤖 机器人启动...` 就表示成功了！

### Step 4: 测试

1. 用另一个账号搜索你的机器人
2. 发送一条消息
3. 你会在你的账号里看到转发
4. 长按消息点回复，用户就能收到你的回复

## 🎉 完成！

现在你的机器人已经可以工作了！

## 📖 更多详情

查看 [README.md](README.md) 了解：
- 详细的部署指南
- 故障排除
- 安全建议
- 扩展功能

## ⚡ 常见快速问题

**Q: 怎么关闭机器人？**
```bash
Ctrl + C
```

**Q: 怎么在后台运行？**
```bash
nohup python3 tg_bot.py > tg_bot.log 2>&1 &
```

**Q: 怎么查看日志？**
```bash
tail -f tg_bot.log
```

**Q: Token 错了怎么办？**
```bash
# 编辑文件，改正 Token，然后重新运行
nano tg_bot.py
python3 tg_bot.py
```

## 需要帮助？

- 📖 查看 [README.md](README.md)
- 🐛 提交 [Issue](https://github.com/yourusername/telegram-forward-bot/issues)
- 💬 讨论 [Discussions](https://github.com/yourusername/telegram-forward-bot/discussions)
