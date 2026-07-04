from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str) -> None:
        pass

class EmailNotifier(NotificationService):
    def send(self, recipient: str, message: str) -> None:
        print(f"[Email] To: {recipient} | {message}")

class SlackNotifier(NotificationService):
    def send(self, recipient: str, message: str) -> None:
        print(f"[Slack] Channel: {recipient} | {message}")

class WebhookNotifier(NotificationService):
    def send(self, recipient: str, message: str) -> None:
        print(f"[Webhook] URL: {recipient} | {message}")

class AlertService:
    def __init__(self, notifier: NotificationService):
        self._notifier = notifier

    def trigger_alert(self, recipient: str, issue: str) -> None:
        alert_message = f"ALERT: {issue}"
        self._notifier.send(recipient, alert_message)


if __name__ == "__main__":
    email_alerts = AlertService(EmailNotifier())
    email_alerts.trigger_alert("ops@company.com", "CPU usage at 95%")

    slack_alerts = AlertService(SlackNotifier())
    slack_alerts.trigger_alert("#incidents", "Database connection pool exhausted")

    webhook_alerts = AlertService(WebhookNotifier())
    webhook_alerts.trigger_alert("https://hooks.example.com/alerts", "Disk usage at 90%")