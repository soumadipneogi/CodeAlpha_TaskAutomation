"""CodeAlpha Task 3 - Task Automation.
Extract all email addresses from a .txt file and save them to another file.
Usage:  python extract_emails.py [input.txt] [output.txt]
"""
import os
import re
import sys

EMAIL_PATTERN = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"


def extract_emails(input_file):
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()
    emails = re.findall(EMAIL_PATTERN, text)
    # remove duplicates, ignore upper/lower case, keep sorted
    return sorted(set(e.lower() for e in emails))


def save_emails(emails, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        for email in emails:
            f.write(email + "\n")


def main():
    # By default use files next to this script, so it works from any folder
    here = os.path.dirname(os.path.abspath(__file__))
    input_file = sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, "sample_input.txt")
    output_file = sys.argv[2] if len(sys.argv) > 2 else os.path.join(here, "emails_found.txt")

    try:
        emails = extract_emails(input_file)
    except FileNotFoundError:
        print(f"Error: '{input_file}' not found.")
        return
    except UnicodeDecodeError:
        print("Error: could not read the file. Save it as UTF-8 text.")
        return

    save_emails(emails, output_file)
    print(f"Found {len(emails)} unique email(s). Saved to '{output_file}':")
    for e in emails:
        print(" -", e)


if __name__ == "__main__":
    main()
