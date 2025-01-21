def split_text(text, chunk_size=1000):
    """Split text into chunks of specified size."""
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    return chunks
