from rank_bm25 import BM25Okapi

class BM25Store:
    def __init__(self, chunks):
        self.bm25 = BM25Okapi([chunk.page_content.split() for chunk in chunks])
        self.chunks = chunks

    def search(self, query, k=5):
        scores = self.bm25.get_scores(query.split())
        top_k = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:k]
        return [self.chunks[i] for i in top_k]
        
    