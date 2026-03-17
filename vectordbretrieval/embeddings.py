from langchain_huggingface import HuggingFaceEmbeddings

def get_embeddings():
    return HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")

def main():
    embeddings = get_embeddings()
    print(embeddings.embed_query("Hello World")) 

if __name__ == "__main__":
    main()