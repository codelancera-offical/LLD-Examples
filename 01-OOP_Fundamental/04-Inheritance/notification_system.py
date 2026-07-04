from datetime import datetime

class Notification:
    def __init__(self, recipient: str, message: str):
        self._recipient = recipient
        self._timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._message = message

    def format_header(self) -> str:
        return f"[{self._timestamp}] To: {self._recipient}"
    
    def send(self):
        print(self.format_header)
        print(f"Message: {self._message}")


class EmailNotification(Notification):
    def __init__(self, recipient: str, message: str, subject: str):

        super().__init__(recipient, message) # 调用父类初始化方法
        self._subject = subject # 多了一个主题

    def send(self):
        print(self.format_header())
        print(f"Subject: {self._subject}")
        print(f"Body: {self._message}")
        print("Status: Email delivered")

class SMSNotification(Notification):
    MAX_LENGTH = 160

    def __init__(self, recipient: str, message: str, phone_number: str):
        super().__init__(recipient, message)
        self._phone_number = phone_number   # 多了一个phone_number

    def send(self):
        print(self.format_header())
        print(f"Phone: {self._phone_number}")
        sms_body = (self._message[:self.MAX_LENGTH - 3] + "..."
                    if len(self._message) > self.MAX_LENGTH
                    else self._message)
        print(f"SMS: {sms_body}")
        print(f"Status: SMS sent ({len(sms_body)}/{self.MAX_LENGTH} chars)")

class PushNotification(Notification):   # 不知道这是啥 没啥概念
    def __init__(self, recipient: str, message: str,
                 device_token: str, priority: str):
        super().__init__(recipient, message)
        self._device_token = device_token
        self._priority = priority

    def send(self):
        print(self.format_header())
        print(f"Device: {self._device_token[:8]}...")
        print(f"Priority: {self._priority}")
        print(f"Alert: {self._message}")
        print("Status: Push notification delivered")

if __name__ == "__main__":
    email = EmailNotification(
        "alice@example.com", "Your order has been shipped!", "Order Update")
    email.send()

    print()

    sms = SMSNotification(
        "Bob", "Your verification code is 482910.", "+1-555-0123")
    sms.send()

    print()

    push = PushNotification(
        "Charlie", "New message from Alice", "d8a3f4b2c1e5a9b7", "high")
    push.send()