import logging
import random

COST_LOG = "/home/keef/alpha-sentinel/engineer/cost_log.md"
DAILY_BUDGET = 5.0  # USD

def monitor_costs():
    # Simulate usage (in a real scenario, fetch usage from APIs)
    usage = random.uniform(0.1, 0.8)
    
    with open(COST_LOG, "a") as f:
        f.write(f"Usage tracked: ${usage:.2f}\n")
    
    if usage > 0.7:
        print("ALERT: High cost detected.")
        # Trigger same escalation logic as sentinel
        
if __name__ == "__main__":
    monitor_costs()
