import requests

# Function to send Telegram notifications
def send_telegram_notification(message):
    bot_token = "7668588130:AAGVDR6rgCEwgfBe67T-9AX1ATAV2fSGlIs"  # Replace with your bot token
    chat_id = "1953281261"  # Replace with your chat ID
    
    url = f"https://api.telegram.org/bot7668588130:AAGVDR6rgCEwgfBe67T-9AX1ATAV2fSGlIs/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Telegram notification sent successfully!")
        else:
            print(f"Failed to send Telegram notification. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending Telegram message: {e}")
