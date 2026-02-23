#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import re

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler('tg_bot.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# ==================== 配置 ====================
ADMIN_ID = 123456789  # 改成你的 User ID
BOT_TOKEN = "123456789:AAEmT-gA9Yw160Jg_mKR-l36Kdp_ESZaPFM"  # 改成你的 Bot Token

# ==================== 命令处理器 ====================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """处理 /start 命令"""
    await update.message.reply_text("👋 欢迎！\n\n直接发送消息给我")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """处理 /help 命令"""
    await update.message.reply_text("💬 发送任何消息，我会转发给主人")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """处理所有消息"""
    user = update.effective_user
    message_text = update.message.text or ""
    
    logger.info(f"用户 {user.id}: {message_text}")
    
    # 如果是管理员（你）发的消息
    if user.id == ADMIN_ID:
        # 检查是否是回复消息
        if update.message.reply_to_message:
            reply_text = update.message.reply_to_message.text
            
            # 从转发的消息里提取用户ID (格式: 👤 用户名 (ID))
            match = re.search(r'\((\d+)\)', reply_text)
            
            if match:
                target_user_id = int(match.group(1))
                
                try:
                    await context.bot.send_message(chat_id=target_user_id, text=message_text)
                    await update.message.reply_text(f"✅ 已回复")
                    logger.info(f"回复给用户 {target_user_id}: {message_text}")
                except Exception as e:
                    logger.error(f"发送失败: {e}")
                    await update.message.reply_text(f"❌ 发送失败: {e}")
            else:
                await update.message.reply_text("❌ 找不到用户ID")
        return
    
    # 普通用户发的消息，转发给管理员
    try:
        forward_text = f"📨 新消息\n\n👤 {user.first_name} ({user.id})\n💬 {message_text}"
        await context.bot.send_message(chat_id=ADMIN_ID, text=forward_text)
    except Exception as e:
        logger.error(f"转发失败: {e}")
    
    await update.message.reply_text("✅ 已接收")

async def error_handler(update, context):
    """错误处理"""
    logger.error(f"异常: {context.error}")

# ==================== 主函数 ====================

def main():
    """启动机器人"""
    app = Application.builder().token(BOT_TOKEN).build()
    
    # 添加处理器
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_error_handler(error_handler)
    
    logger.info("🤖 机器人启动...")
    app.run_polling()

if __name__ == '__main__':
    main()
