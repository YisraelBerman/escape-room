import imaplib
import email
import requests
import time

# Email login details
email_user = 'jenkinstrigger@outlook.co.il'
email_pass = 'yis12345'
imap_url = 'imap-mail.outlook.com'

# Connect to the email server
try:
    mail = imaplib.IMAP4_SSL(imap_url)
    mail.login(email_user, email_pass)
    mail.select('inbox')
    print("Connected to the email server successfully.")
except Exception as e:
    print(f"Failed to connect to email server: {e}")
    exit()

def check_email():
    status, messages = mail.search(None, 'UNSEEN')
    if status != 'OK':
        print("Failed to search emails.")
        return

    if not messages[0]:
        print("No unseen emails found.")
        return
    
    for num in messages[0].split():
        status, data = mail.fetch(num, '(RFC822)')
        if status != 'OK':
            print(f"Failed to fetch email {num}.")
            continue
        
        msg = email.message_from_bytes(data[0][1])
        print(f"Found email with subject: {msg['subject']}")

        # Check if the subject matches
        if 'Trigger Jenkins Job' in msg['subject']:
            print("Triggering Jenkins job...")
            trigger_jenkins_job()
        else:
            print("No matching subject found.")

def trigger_jenkins_job():
    jenkins_url = 'http://jenkins-server-url/job/your-job-name/build'
    try:
        response = requests.post(jenkins_url, auth=('your-jenkins-username', 'your-api-token'))
        if response.status_code == 201:
            print("Jenkins job triggered successfully.")
        else:
            print(f"Failed to trigger Jenkins job. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error triggering Jenkins job: {e}")


if __name__ == "__main__":
    while True:
        check_email()
        time.sleep(60)  # Wait for 60 seconds before checking again
