# Architecture

```
                    Next.js

         Chat • Dashboard • Maps

                    │

                FastAPI API

 ┌─────────────────────────────────────┐
 │ Auth Service                        │
 │ Crime Service                       │
 │ Analytics Service                   │
 │ AI Service                          │
 └─────────────────────────────────────┘

                    │

             LangGraph Agent

                    │

       ┌────────────┴────────────┐

      SQL Tool           Vector Tool

       │                       │

 PostgreSQL              pgVector
```

## Components

- Frontend
- Backend
- AI Agent
- PostgreSQL
- pgVector

The AI Agent selects tools based on the user's query instead of directly answering.