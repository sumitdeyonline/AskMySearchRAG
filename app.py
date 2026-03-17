import streamlit as st

from pathlib import Path
from ingestion.ingest import load_documents
from vectordbretrieval.vector_store import VectorStore
from vectordbretrieval.BM25_store import BM25Store
from vectordbretrieval.embeddings import get_embeddings
from vectordbretrieval.hybrid import hybrid_search
from rerank.reranker import Reranker
from rag.contextprompt import build_context_prompt
from rag.llmanswer import RAG
import os
# import os
# from dotenv import load_dotenv

# load_dotenv()
# os.environ["TOKENIZERS_PARALLELISM"] = "false"
# 1. Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# 2. Callback function to clear the output when the user hits 'Enter'
def clear_output():
    st.session_state.messages = []
def main():
    st.title("🔎 Ask My Search RAG")
    #question = "What is AI?"
    question = st.text_input("Ask a Question")
    print("Question\n")
    print(question)
    
    if "history" not in st.session_state:
        st.session_state.history = []

    if st.button("Search"):
        output_container = st.empty()
        if question.strip() == "":
            st.warning("Please enter a question.")
        else:
            with st.spinner("Researching..."):
                #print("Hello from askmysearchrag!")
                #print("Loading documents..."+ str(Path(__file__).parent))
                data_dir = Path(__file__).parent / "data"
                chunks = load_documents(data_dir)
                #chunks = split_documents(documents)
                # for chunk in chunks:
                #     print(f"Chunk{len(chunk)}: {chunk}")
                embeddings = get_embeddings()
                vs = VectorStore()

                if os.path.exists("./chroma_db") and os.listdir("./chroma_db"):
                    print("Vector store already exists in ./chroma_db. Skipping creation...")
                else:
                    print("Vector store not found. Creating new...")
                    vs.storeIntoVectorStore(chunks,embeddings)
                    
                # Search the vector store
                search = vs.searchFromVectorStore(question)
                #print(search)
                #print(search[0].page_content)
                #print("File : "+search[0].metadata["source"])
                bm25_store = BM25Store(chunks)
                # Search the BM25 store
                #print("BM25 Search\n")
                search = bm25_store.search(question)
                #print(search)
                #print(search[0].page_content)
                #print("File : "+search[0].metadata["source"])

                hybrid_results = hybrid_search(vs,bm25_store,question)

                # for i in hybrid_results:
                #     print(i.page_content)
                #     print("File : "+i.metadata["source"])

                reranker = Reranker()
                reranked_results = reranker.rerank(question, hybrid_results)
                # for i in reranked_results:
                #     print(i.page_content)
                #     print("File : "+i.metadata["source"])


                prompt = build_context_prompt(question, reranked_results)
                #print(prompt)

                rag = RAG()
                answer = rag.generate(question, prompt)
                print("Answer\n")
                print(answer)


                # ✅ Save to history
                st.session_state.history.append({
                    "question": question,
                    "answer": answer,
                    "sources": [doc.metadata.get("source", "Unknown") for doc in reranked_results]
                })

                with output_container.container():
                    st.subheader("Answer")
                    st.write(answer)
                    st.subheader("Sources")
                    for i, doc in enumerate(reranked_results):
                        #st.write(i.metadata["source"])
                        st.markdown(f"**[{i}]** {doc.metadata.get('source', 'Unknown')}")
                        st.caption(doc.page_content[:300] + "...")
                        # print(hybrid_results[0].page_content)
                        # print(hybrid_results[1].page_content)
                # Display chat history
                with st.sidebar:
                    if st.session_state.history:
                        st.subheader("History")
                        for i, msg in enumerate(st.session_state.history):
                            with st.expander(f"Question {i+1}: {msg['question']}"):
                                st.write(f"**Answer:** {msg['answer']}")
                                st.write(f"**Sources:** {', '.join(msg['sources'])}")

if __name__ == "__main__":
    main()
