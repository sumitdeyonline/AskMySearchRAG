def hybrid_search(vector_store, bm25_store, query, k=5):
    vector_results = vector_store.searchFromVectorStore(query, k)
    bm25_results = bm25_store.search(query, k)
    docs = vector_results + bm25_results
    unique = {doc.page_content: doc for doc in docs}
    return list(unique.values())
    # return vector_results + bm25_results