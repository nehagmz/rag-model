from sentence_transformers import SentenceTransformer, util

# Load the transformer model (once, globally)
model = SentenceTransformer('all-MiniLM-L6-v2')

def retrieve_relevant_chunks(question, text_chunks, similarity_threshold=0.4):
    """
    Retrieve relevant chunks using semantic similarity.
    
    Args:
        question (str): The user's question.
        text_chunks (list): List of text chunks from the document.
        similarity_threshold (float): Minimum similarity score to consider a chunk relevant.
    
    Returns:
        str: Concatenated relevant chunks or an empty string if no relevant chunks found.
    """
    question_embedding = model.encode(question, convert_to_tensor=True)
    chunk_embeddings = model.encode(text_chunks, convert_to_tensor=True)
    
    similarities = util.pytorch_cos_sim(question_embedding, chunk_embeddings)[0]
    
    # Filter chunks above the similarity threshold
    relevant_chunks = [
        text_chunks[i] for i, score in enumerate(similarities) if score >= similarity_threshold
    ]
    
    if not relevant_chunks:
        return ""  # No relevant chunks found
    
    return " ".join(relevant_chunks)
