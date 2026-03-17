# AskMySearchRAG

Build a domain-specific "Ask My Docs" system with hybrid retrieval (BM25 + vector search), cross-encoder reranking, citation enforcement, and a CI-gated evaluation pipeline.

Below is a production-style architecture for building a Domain-Specific “Ask My Docs” RAG system with:

- **Hybrid Retrieval** (BM25 + Vector Search)
- **Cross-Encoder Re-ranking**
- **Evaluation Pipeline** with CI gating

This design is commonly used in enterprise AI search systems.

## Tech Stack

Recommended stack:

- **Docs loading**: LangChain 
- **Vector DB**: Chroma
- **BM25 search**: ElasticSearch
- **Embedding**: HuggingFaceEmbeddings
- **Cross encoder**: CrossEncoder
- **LLM**: OpenAI
- **Evaluation**: Ragas

---

🔗 **UI:** Built with [Streamlit](https://askmysearchrag.streamlit.app/)