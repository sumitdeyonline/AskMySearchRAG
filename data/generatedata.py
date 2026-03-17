import os

topics = {
    "artificial_intelligence.txt": """
Artificial Intelligence (AI) refers to the simulation of human intelligence in machines.
AI systems can perform tasks such as learning, reasoning, problem solving, perception, and language understanding.
Applications include autonomous vehicles, chatbots, recommendation systems, and healthcare diagnostics.
""",

    "machine_learning.txt": """
Machine Learning (ML) is a subset of Artificial Intelligence that allows systems to learn from data.
ML algorithms identify patterns in data and improve performance over time without being explicitly programmed.
Common algorithms include linear regression, decision trees, and neural networks.
""",

    "deep_learning.txt": """
Deep Learning is a subset of machine learning based on artificial neural networks with multiple layers.
It is widely used in computer vision, speech recognition, and natural language processing.
Popular frameworks include TensorFlow and PyTorch.
""",

    "natural_language_processing.txt": """
Natural Language Processing (NLP) enables computers to understand and process human language.
Applications include chatbots, translation systems, sentiment analysis, and text summarization.
Modern NLP models use transformer architectures.
"""
}

# Create folder
#os.makedirs("ai_ml_text_files", exist_ok=True)

# Generate files
for filename, content in topics.items():
    with open(f"./{filename}", "w") as f:
        f.write(content.strip())

print("AI/ML text files generated successfully!")
