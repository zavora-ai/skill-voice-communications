# Voice & Communications Skill

> Voice operations for AI agents — calls, transcription, sentiment analysis, IVR management, recordings, and call center analytics via Twilio, Vonage, and Deepgram.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![MCP Server](https://img.shields.io/badge/mcp--server-mcp--voice-green)](https://github.com/zavora-ai/mcp-voice)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

| Workflow | Calls | Revenue Impact |
|----------|-------|---------------|
| Post-Call Intelligence | 3 | Action items from every call |
| Call Center Monitoring | 2-3 | Queue health + agent performance |
| Sentiment Analysis | 1 | Detect unhappy customers early |
| IVR Management | 2 | Optimize call routing |
| Transcript Search | 1 | Find any conversation by keyword |

### Without this skill:
- Call outcomes forgotten (no transcript)
- Negative sentiment undetected until churn
- IVR changes require vendor support
- No searchable call history

### With this skill:
- Every call transcribed + summarized + sentiment-analyzed
- Negative sentiment on VIP calls triggers immediate alert
- IVR updated directly by agent
- Full transcript search across all calls

## Installation

```bash
git clone https://github.com/zavora-ai/skill-voice-communications.git ~/.skills/skills/voice-communications
```

## Requirements

**Required:** `mcp-voice` (20 tools — Twilio + Vonage + Deepgram)
**Cross-MCP:** `mcp-crm` (auto-log calls), `mcp-slack` (queue alerts), `mcp-customer-service` (sentiment escalation)

## Success Criteria

| Metric | Target |
|--------|--------|
| Transcription | Every call transcribed |
| Sentiment | Analyzed on all customer calls |
| CRM logging | Call summaries auto-logged |
| Search | Find any call by keyword |

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;"/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0 — Part of [ADK-Rust Enterprise](https://enterprise.adk-rust.com). Built with ❤️ by [Zavora AI](https://zavora.ai)
