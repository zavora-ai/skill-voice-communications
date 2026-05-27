# Voice Cross-MCP Workflows

## Voice + CRM: Auto-Log Calls
```
VOICE: get_call_summary(id) → action items
CRM: create_activity(type: "call", description: summary)
```

## Voice + Slack: Queue Alerts
```
VOICE: list_queues() → {wait_time: "8 min", depth: 12}
SLACK: send_message(channel: "#support", text: "⚠️ Queue depth: 12, avg wait: 8 min")
```
