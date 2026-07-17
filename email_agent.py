import csv
import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "raghavendrapatne39@gmail.com"
SENDER_PASSWORD = "koseoeybqusmpfkl"

EMAIL_TEMPLATE = """\
Hi {Name},

Welcome to Exposys Data Labs Coding Round!

Regards,
HR Team
"""


def load_customers(csv_path):
    customers = []
    try:
        with open(csv_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row.get("Name", "").strip()
                email = row.get("Email", "").strip()
                if name and email:
                    customers.append({"Name": name, "Email": email})
    except FileNotFoundError:
        print(f"Error: File '{csv_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading CSV: {e}")
        sys.exit(1)
    return customers


def personalize(template, data):
    body = template
    for key, value in data.items():
        body = body.replace(f"{{{key}}}", value)
    return body


def send_email(recipient_name, recipient_email, subject, body):
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, recipient_email, msg.as_string())
        return True
    except smtplib.SMTPAuthenticationError:
        print("  SMTP authentication failed. Check email/password.")
        return False
    except smtplib.SMTPRecipientsRefused:
        print(f"  Recipient refused: {recipient_email}")
        return False
    except Exception as e:
        print(f"  Send error: {e}")
        return False


def main():
    csv_path = sys.argv[1] if len(sys.argv) > 1 else "customers.csv"
    dry_run = "--dry-run" in sys.argv
    subject = "Welcome to Exposys Data Labs!"

    customers = load_customers(csv_path)
    if not customers:
        print("No customers found in CSV.")
        return

    print(f"Loaded {len(customers)} customer(s) from '{csv_path}'")
    if dry_run:
        print("(Dry-run mode: emails will NOT be sent)\n")

    sent = 0
    failed = 0

    for customer in customers:
        body = personalize(EMAIL_TEMPLATE, customer)
        print(f"To: {customer['Email']} ({customer['Name']})")

        if dry_run:
            print(f"  [DRY-RUN] Would send:\n{body}")
            sent += 1
        else:
            success = send_email(customer["Name"], customer["Email"], subject, body)
            if success:
                print("  Status: Sent")
                sent += 1
            else:
                print("  Status: Failed")
                failed += 1

        print()

    print(f"--- Summary ---")
    print(f"Sent: {sent}  |  Failed: {failed}  |  Total: {len(customers)}")


if __name__ == "__main__":
    main()
