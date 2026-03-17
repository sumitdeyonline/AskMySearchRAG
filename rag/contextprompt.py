from langchain_core.prompts import ChatPromptTemplate


def build_context_prompt(query, docs):
    
    context = build_context(docs)
    template = ChatPromptTemplate.from_template(
        """
        You are a helpful assistant.
        Use ONLY the provided context.
        Provide citations using [number].
        If the answer is not in the context, say "I don't know".
        Context: {context}
        Question: {query}
        Answer with citations like [0], [1].
        """
    )
    return template.format(context=context, query=query)




def build_context(docs):

    context = ""

    for i, doc in enumerate(docs):
        context += f"[{i}] {doc.page_content}\n"
    
    return context