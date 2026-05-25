import re
import os
import subprocess

LOG_FILE = "/home/keef/alpha-sentinel/engineer/sentinel_logs.log"
REMEDIATION_LOG = "/home/keef/alpha-sentinel/engineer/remediation_log.md"
ALERT_WINDOW = "/home/keef/alpha-sentinel/engineer/alert_window.html"
EMAIL_RECIPIENT = "kwizzlesurp10@gmail.com"

def send_email_alert(subject, body):
    cmd = f'echo "{body}" | himalaya template send --header "To:{EMAIL_RECIPIENT}" --header "Subject:{subject}"'
    subprocess.run(cmd, shell=True)

def analyze_errors():
    if not os.path.exists(LOG_FILE):
        return

    with open(LOG_FILE, "r") as f:
        logs = f.readlines()

    for line in logs:
        if "ERROR" in line or "CRITICAL" in line:
            # Generate remediation
            with open(REMEDIATION_LOG, "a") as r:
                r.write(f"## Error Found: {line}\n")
                r.write("- **Hypothesis**: Likely network instability or API key expiration.\n")
                r.write("- **Action**: Check `TELEGRAM_TOKEN` and connection stability.\n")
            
            # Pop standalone notification window
            # Check return code for failure
            proc = subprocess.Popen(["xdg-open", ALERT_WINDOW])
            if proc.wait() != 0:
                print("Pop-up failed. Sending email alert...")
                send_email_alert("Alpha Sentinel Critical Alert", f"Error detected: {line}\nRemediation: Check /home/keef/alpha-sentinel/engineer/remediation_log.md")
            
            print("Remediation suggestion generated and ALERT attempted.")

if __name__ == "__main__":
    analyze_errors()
