from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path

from langchain_core.documents import Document

def load_documents(folder: str):
    """Load documents from the data directory."""
    docs = []
    print(f"Loading documents from {Path(folder)}")
    for file in Path(folder).glob("*.txt"):
        with open(file, "r", encoding="utf-8") as f:
            docs.append(Document(page_content=f.read(), metadata={"source": file.name}))
    splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ".", " "],
        chunk_size=800,
        chunk_overlap=150,
        #length_function=len,
        #is_separator_regex=False,
    )
    
    chunks = splitter.split_documents(docs)

    # Return the Langchain Document objects directly for compatibility with Chroma store
    return chunks


def main():
    print("Loading documents...")
    data_dir = Path(__file__).parent.parent / "data"
    chunks = load_documents(data_dir)
    #chunks = split_documents(documents)
    for chunk in chunks:
        print(f"Chunk{len(chunk)}: {chunk}")
    #print(f"Loaded {len(documents)} documents and split into {len(chunks)} chunks.")

if __name__ == "__main__":
    main()