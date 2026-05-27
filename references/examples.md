# Voice Examples

## Example 1: "What was discussed on the last call with Acme?"
```
search_transcripts(query: "Acme") → [{call_id: "call_123", snippet: "...pricing discussion..."}]
get_transcript(call_id: "call_123") → full transcript with speakers
get_call_summary(call_id: "call_123") → "Discussed Enterprise pricing. Sarah wants proposal by Friday."
```
Response: "Last call with Acme (12 min): Discussed Enterprise pricing. Action: Send proposal by Friday."

## Example 2: "How's the call center performing?"
```
get_call_metrics() → {volume: 234, avg_duration: "4:30", answer_rate: 92%}
get_agent_stats() → [{agent: "Tom", calls: 45, avg_sentiment: 0.7}, ...]
get_sentiment_trends(period: "7d") → {trend: "improving", avg: 0.72}
```
Response: "234 calls today, 92% answer rate. Sentiment trending up (0.72 avg). Top agent: Tom (45 calls)."
