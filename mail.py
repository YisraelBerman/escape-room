import sys
import imaplib
import email
import requests
import time

# Check if the correct number of arguments is provided
if len(sys.argv) != 6:
    print("Usage: python your_script.py <email_password> <jenkins_url> <jenkins_user> <jenkins_token> <jenkins_crumb>")
    print("Note: If your Jenkins instance doesn't require a crumb, you can pass 'none' as the jenkins_crumb.")
    sys.exit(1)

# Email login details
email_user = 'jenkinstrigger@outlook.co.il'
email_pass = sys.argv[1]  # Fetch the email password from the command-line argument
imap_url = 'imap-mail.outlook.com'

# Jenkins details
jenkins_base_url = sys.argv[2]  # Base Jenkins URL
jenkins_user = sys.argv[3]
jenkins_token = sys.argv[4]
jenkins_crumb = sys.argv[5] if sys.argv[5].lower() != 'none' else None

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
        subject = msg['subject']  # Correctly extract the subject
        print(f"Found email with subject: {subject}")

        # Check if the subject matches the expected pattern
        if 'Trigger Jenkins Job:' in subject:
            project_name = subject.split(':')[-1].strip()  # Extract the project name
            print(f"Triggering Jenkins job for project: {project_name}")
            trigger_jenkins_job(jenkins_base_url, jenkins_user, jenkins_token, project_name, jenkins_crumb)
        else:
            print("No matching subject found.")

def trigger_jenkins_job(jenkins_base_url, jenkins_user, jenkins_token, project_name, jenkins_crumb=None):
    job_url = f"{jenkins_base_url}/job/{project_name}/build"  # Construct the Jenkins job URL
    headers = {}
    
    if jenkins_crumb:
        headers['Jenkins-Crumb'] = jenkins_crumb
    
    try:
        response = requests.post(job_url, auth=(jenkins_user, jenkins_token), headers=headers)
        if response.status_code == 201 or response.status_code == 200:
            print(f"Jenkins job '{project_name}' triggered successfully.")
        else:
            print(f"Failed to trigger Jenkins job '{project_name}'. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error triggering Jenkins job '{project_name}': {e}")

if __name__ == "__main__":
    while True:
        check_email()
        time.sleep(60)  # Wait for 60 seconds before checking again
