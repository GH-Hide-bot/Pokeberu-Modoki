# 🗺️ PROJECT MAP & STATUS

## 1. 🌀 システム相関図 (System Correlation Diagram)

```mermaid
graph TD
    User[Hide-kun] <--> NLM[NLM/Anti (AI Persona/Assistant)]
    NLM <--> RAM[RAM (Central AI / Executor)]
    RAM <--> VertexAI[Vertex AI Extensions / Memory & Code Exec]
    NLM --> AutoLog[AtelierTSA_AutoLog.py]
    AutoLog --> Brainstorm[00_index:BRAINSTORM_LIST.md]
    AutoLog --> MapStatus[00_MAP_AND_STATUS.md]
    User --> PagerUI[Pager UI (Canva/Web Interface)]
    PagerUI <--> LocalServer[M1 Mac (192.168.11.6)]
    VertexAI <--> LocalServer
    VertexAI <--> ExternalAPI[External APIs / Documentation]
```

## 2. 📐 現在の設計図 (Current Design Specs)

- **Concept**: Fully autonomous dev platform driven by RAM & NLM/Anti.
- **Interface**: Pager-style Web UI (nostalgic/premium).
- **Core Engine**: RAM with Long-term Memory & Code Execution rights.
- **Protocol**: Anti-v2 "Physical Layer Landing" via Vertex AI Extensions.

## 3. 🚦 プロジェクトの進行ステータス (Project Status)

- [x] Phase 1: Basic Infrastructure & Logging (Anti-v2)
- [x] Phase 2: System Mapping & Documentation Consolidation
- [/] Phase 3: RAM Evolution & Vertex AI Integration (Current Focus)
- [ ] Phase 4: Pager UI Implementation & Mobile Access

---
*Updated by NLM/Anti at 2026/03/24 11:17:00*
