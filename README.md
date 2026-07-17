
 # Email Agent

A Python script that sends personalized emails to multiple recipients using data from a CSV file. Built for Exposys Data Labs to automate welcome emails during the coding round process.

## Features

- Reads recipient data (Name, Email) from a CSV file
- Personalizes email templates with recipient details
- Sends emails via Gmail SMTP with TLS encryption
- Supports dry-run mode for testing without sending emails
- Provides a summary of sent/failed emails after completion

## Prerequisites

- Python 3.6+
- A Gmail account with an App Password (not your regular password)

### Setting Up Gmail App Password

1. Go to your Google Account settings
2. Enable 2-Step Verification
3. Navigate to **Security > App passwords**
4. Generate a new app password and use it in the script

## Usage

```bash
# Send emails to all customers in the default CSV
python email_agent.py

# Specify a different CSV file
python email_agent.py path/to/customers.csv

# Test without actually sending emails
python email_agent.py --dry-run

# Combine both options
python email_agent.py path/to/customers.csv --dry-run
```

## CSV Format

The input CSV file must have the following columns:

```csv
Name,Email
John,john@example.com
Jane,jane@example.com
```

## Configuration

Update the following constants in `email_agent.py`:

| Variable | Description |
|---|---|
| `SMTP_SERVER` | SMTP server address (default: `smtp.gmail.com`) |
| `SMTP_PORT` | SMTP port (default: `587`) |
| `SENDER_EMAIL` | Your Gmail address |
| `SENDER_PASSWORD` | Your Gmail app password |
| `EMAIL_TEMPLATE` | The email body template with `{Name}` placeholder |

## Project Structure

```
.
├── email_agent.py     # Main script
├── customers.csv      # Sample customer data
└── README.md
```

## License

This project is for educational purposes as part of the Exposys Data Labs Coding Round.

