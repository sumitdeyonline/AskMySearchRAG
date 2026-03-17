import chromadb
from sentence_transformers import SentenceTransformer
from langchain_chroma import Chroma

class VectorStore:
    # def __init__(self):
    #     self.client = chromadb.Client()
    #     self.collection = self.client.get_or_create_collection(name="rag_collection")
    #     self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def storeIntoVectorStore(self, chunks,embedding):
        vectorStore = Chroma.from_documents(
            documents=chunks,
            embedding=embedding,
            collection_name="rag_collection",
            persist_directory="./chroma_db"
        )
        return vectorStore

    def searchFromVectorStore(self, query, k=5):
        vectorStore = Chroma(
            collection_name="rag_collection",
            persist_directory="./chroma_db"
        )
        return vectorStore.similarity_search(query, k) 
    def searchFromVectorStoreWithScore(self, query, k=5):
        vectorStore = Chroma(
            collection_name="rag_collection",
            persist_directory="./chroma_db"
        )
        return vectorStore.similarity_search_with_score(query, k) 

    def searchFromVectorStoreWithMetadata(self, query, k=5):
        vectorStore = Chroma(
            collection_name="rag_collection",
            persist_directory="./chroma_db"
        )
        return vectorStore.similarity_search_with_metadata(query, k) 

    def deleteVectorStore(self):
        try:
            client = chromadb.PersistentClient(path="./chroma_db")
            client.delete_collection("rag_collection")
        except ValueError:
            pass # Collection does not exist

    

    # def build_vector_store(self, chunks):
    #     embeddings = self.model.encode([chunk["text"] for chunk in chunks])
    #     self.collection.add(
    #         embeddings=embeddings,
    #         documents=[chunk["text"] for chunk in chunks],
    #         metadatas=[{"source": chunk["source"]} for chunk in chunks],
    #         ids=[str(i) for i in range(len(chunks))]
    #     )

    def search(self, query, k=5):
        embedding = self.model.encode([query])
        results = self.collection.query(
            query_embeddings=embedding,
            n_results=k
        )
        return results