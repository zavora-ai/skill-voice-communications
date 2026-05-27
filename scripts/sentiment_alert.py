#!/usr/bin/env python3
"""Determine if a call sentiment requires escalation."""
import json, sys

def assess(data):
    customer_sentiment = data.get("customer_sentiment", 0)
    customer_plan = data.get("plan", "free")
    health = data.get("health", 100)
    escalate = customer_sentiment < -0.3 and (customer_plan == "enterprise" or health < 50)
    return {"escalate": escalate, "reason": "Negative sentiment + high-value customer" if escalate else "OK",
            "sentiment": customer_sentiment, "plan": customer_plan}

if __name__ == "__main__":
    print(json.dumps(assess(json.loads(sys.argv[1])), indent=2))
