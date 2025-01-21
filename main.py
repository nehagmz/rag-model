from src.extract_pdf import extract_text_from_pdf
from src.text_processing import split_text
from src.retrieval import retrieve_relevant_chunks
from src.answer_generation import get_answer

if __name__ == "__main__":
    pdf_path = "data/input.pdf"  # Path to your PDF file
    
    try:
        pdf_text = extract_text_from_pdf(pdf_path)  # Extract text from the PDF
        text_chunks = split_text(pdf_text)  # Split the text into chunks
        
        print("PDF loaded successfully. You can now ask questions based on its content.")
        
        while True:
            question = input("Ask a question: ").strip()  # User input for question
            
            if not question:
                print("Please enter a valid question.")
                continue
            
            # Retrieve relevant context from PDF based on the question
            context = retrieve_relevant_chunks(question, text_chunks)
            
            # Generate the answer using the context from the PDF
            answer = get_answer(question, context)
            print("Answer:", answer)
            
            # Ask the user if they want to ask another question
            continue_asking = input("Do you want to ask another question? (yes/no): ").strip().lower()
            if continue_asking != "yes":
                print("Exiting the RAG system. Goodbye!")
                break

    except Exception as e:
        print(f"An error occurred: {e}")
