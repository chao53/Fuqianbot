from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# === 替换为你从 BotFather 获取的 token ===
BOT_TOKEN = "7983450617:AAGI0cErLXI7StsL0HZiJSttEuf8BjwZ_Dw"

# /start 命令的处理函数
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 你好，星言！2")

# /help 命令的处理函数
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📌 发送 /start 来开始使用这个机器人。")

# 主程序入口
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("🤖 机器人已启动... Ctrl+C 可停止")
    app.run_polling()

if __name__ == "__main__":
    main()
