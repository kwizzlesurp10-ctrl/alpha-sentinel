import os
import subprocess
import logging

logging.basicConfig(level=logging.INFO)

def deploy_factory():
    token = os.getenv("VERCEL_TOKEN")
    if not token:
        logging.error("VERCEL_TOKEN environment variable is not set. Deployment aborted.")
        return

    logging.info("Initiating Vercel deployment for Alpha Sentinel via Vercel CLI...")
    
    try:
        # Use npx vercel for robust project building and deployment
        result = subprocess.run(
            ["npx", "vercel", "--token", token, "--prod", "--yes"],
            cwd="/home/keef/alpha-sentinel",
            capture_output=True,
            text=True,
            check=True
        )
        logging.info("Deployment successful!")
        for line in result.stderr.split('\n'):
            if "Production" in line and "https://" in line:
                logging.info(line.strip())
            elif "Aliased" in line and "https://" in line:
                logging.info(line.strip())
                
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to trigger Vercel deployment.")
        logging.error(f"Command output: {e.stderr}")

if __name__ == "__main__":
    deploy_factory()
