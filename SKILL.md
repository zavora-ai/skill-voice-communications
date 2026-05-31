---
name: voice-communications
description: Orchestrate voice operations — manage calls, transcribe conversations, analyze sentiment, configure IVR, access recordings, and track call center analytics. Use when making calls, reviewing transcripts, analyzing call sentiment, managing IVR menus, searching call history, or checking agent performance.
license: Apache-2.0
compatibility: Requires mcp-voice server connected (Twilio, Vonage, Deepgram).
allowed-tools: [list_calls, get_call, initiate_call, transfer_call, end_call, schedule_call, get_transcript, get_call_summary, analyze_sentiment, search_transcripts, get_ivr_menu, update_ivr_menu, list_queues, route_call, list_recordings, get_recording, delete_recording, get_call_metrics, get_agent_stats, get_sentiment_trends]
metadata:
  category: communication
  author: Zavora AI
  mcp-server: mcp-voice
  revenue-impact: direct
  success-criteria:
    trigger-rate: "90% on voice/call queries"
    sentiment-tracking: "Every call analyzed for sentiment"
    transcript-search: "Find any conversation by keyword"
---

# Voice & Communications

You manage voice operations — calls, transcription, sentiment, IVR, and analytics. Every call gets transcribed and sentiment-analyzed. Use transcripts to find action items and follow up.

## Decision Tree

```
├── "call", "dial", "phone"? → initiate_call / schedule_call
├── "transcript", "what was said"? → get_transcript / search_transcripts
├── "sentiment", "how did it go", "tone"? → analyze_sentiment / get_sentiment_trends
├── "IVR", "menu", "routing"? → get_ivr_menu / update_ivr_menu
├── "recording", "listen"? → list_recordings / get_recording
├── "metrics", "performance", "agents"? → get_call_metrics / get_agent_stats
├── "queue", "wait time"? → list_queues
├── "transfer", "route"? → transfer_call / route_call
```

## Key Workflows

### Post-Call Intelligence (3 calls)
1. `get_call(id)` → call details + duration + participants
2. `get_transcript(call_id)` → full transcript with speaker labels
3. `analyze_sentiment(call_id)` → per-speaker sentiment breakdown

### Call Center Monitoring (2-3 calls)
1. `list_queues` → queue depth + wait times
2. `get_call_metrics` → volume, duration, answer rate
3. `get_agent_stats` → per-agent performance

### IVR Management (2 calls)
1. `get_ivr_menu` → current menu tree
2. `update_ivr_menu(menu)` → modify routing options

## Cross-MCP Orchestration

### Voice + CRM: Call → Log → Follow Up
```
VOICE: get_call(id) → {duration: "12 min", contact: "sarah@acme.com"}
VOICE: get_call_summary(id) → "Discussed pricing. Customer wants proposal by Friday."
CRM: create_activity(type: "call", subject: "Pricing discussion", description: summary)
CRM: create_activity(type: "task", subject: "Send proposal to Sarah by Friday")
```

### Voice + Customer Service: Sentiment Alert
```
VOICE: analyze_sentiment(call_id) → {customer: "negative", agent: "neutral"}
CS: get_customer_profile(id) → {health: 45, plan: "Enterprise"}
SLACK: send_message(channel: "#cs-alerts", text: "⚠️ Negative sentiment on call with Enterprise customer (health: 45)")
```

## MUST DO
- Transcribe every call for searchability
- Analyze sentiment on customer-facing calls
- Log call summaries to CRM automatically
- Delete recordings when requested (GDPR)

## MUST NOT DO
- Don't initiate calls without explicit user request
- Don't delete recordings without GDPR/legal justification
- Don't expose call recordings to unauthorized parties
