---

# RAG System: PDF-Based Question Answering

This project implements a **Retrieval-Augmented Generation (RAG)** system that allows users to ask questions based on the content of a given PDF document. The system retrieves relevant context from the document and generates answers using a language model.

## Features

- Extracts text from PDFs using **PyMuPDF** (`fitz`).
- Splits extracted text into manageable chunks.
- Retrieves relevant information using semantic similarity (via `SentenceTransformer`).
- Generates precise answers using **Llama 2** through the **Ollama CLI**.
- Handles irrelevant queries gracefully by responding with "Sorry, this information is not mentioned in the given document."

## Directory Structure

```
rag-system/
├── main.py                # Entry point for the RAG system
├── answer_generation.py   # Generates answers using Llama 2
├── extract_pdf.py         # Extracts text from PDF documents
├── text_processing.py     # Splits extracted text into chunks
├── retrieval.py           # Retrieves relevant chunks using semantic similarity
├── data/
│   └── input.pdf          # The PDF document to process
└── README.md              # Project documentation
```

## Prerequisites

1. **Python 3.8 or higher**: Ensure Python is installed.
2. **Virtual Environment**: Recommended for dependency isolation.
3. **Llama 2 via Ollama CLI**: Install and set up the Ollama CLI for querying Llama 2.
4. **Dependencies**: Install the required Python libraries:
   - `PyMuPDF`
   - `sentence-transformers`
   - `torch`

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/rag-system.git
cd rag-system
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv rag_env
source rag_env/bin/activate  # On Windows: rag_env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Install and Configure Ollama CLI
Follow the instructions to install the Ollama CLI and set up **Llama 2**:
- [Ollama CLI Installation Guide](https://ollama.ai)

### 5. Add the PDF Document
Place your PDF file in the `data/` directory. Rename it to `input.pdf` or update the path in `main.py`.

## How to Run

1. Activate the virtual environment:
   ```bash
   source rag_env/bin/activate  # On Windows: rag_env\Scripts\activate
   ```

2. Run the main script:
   ```bash
   python main.py
   ```

3. Follow the prompts to ask questions about the PDF content.

## Example Session

Below is a sample output when the system is run:

```plaintext
(rag_env) PS C:\Users\<username>\Desktop\rag-system> python -u "c:\Users\<username>\Desktop\rag-system\main.py"
PDF loaded successfully. You can now ask questions based on its content.
Ask a question: monkeys
Answer: Sorry, this information is not mentioned in the given document.
Do you want to ask another question? (yes/no): yes
Ask a question: specifications
Answer: The specifications for the Ford EcoSport include:

* Fuel consumption: L/100km (mpg) - ØØ, Power (PS) - 125, CO2 (g/km) - 6.6, Urban, Extra Urban, Combined, Max speed (kph/mph) - 180 (112), 0-100 kph (sec) - 12.7, 50-100 kph (sec)* - 12.8
* Engine: 1.0-litre EcoBoost (5-speed manual) - 125, 1.5-litre Ti-VCT (5-speed manual) - 112, 1.5-litre Ti-VCT (6-speed automatic) - 112
* Transmission: 5-speed manual, 6-speed automatic
* Cylinders: 4 in line
* Displacement: cm3 - 1498
* Bore: mm - 73.5, Stroke: mm - 88.3
* Compression ratio: 16.0:1
* Max power (PS/kW) - 95, Max torque (Nm) - 215
* Valve gear: DOHC with 2 valves per cylinder
* Cylinder head: Cast aluminium
* Cylinder block: Cast aluminium
* Camshaft drive: Timing belt (crankshaft to intake) with dynamic tensioner; intake to exhaust chain with hydraulic tensioner
* Engine management: Ford Common Rail Diesel Engine Management System
* Fuel injection: Common rail direct fuel injection; 1600 bar injection pressure; 7-hole piezo-electric injectors
* Emission control: Oxidation catalyst, water-cooled EGR, and standard CDPF

Note: The information provided is based on the given document and may not be comprehensive or up-to-date.
Do you want to ask another question? (yes/no): no
Exiting the RAG system. Goodbye!
```

## Key Modules

- **`extract_pdf.py`**: Extracts text from the PDF document using `PyMuPDF`.
- **`text_processing.py`**: Splits the extracted text into smaller chunks (default: 1000 characters).
- **`retrieval.py`**: Finds the most relevant chunks for a given question using `SentenceTransformer` and cosine similarity.
- **`answer_generation.py`**: Generates answers using Llama 2 and the Ollama CLI.

## Troubleshooting

- **Incomplete or unclear answers**:
  - Ensure the PDF contains well-structured text.
  - Verify the Ollama CLI is properly installed and accessible.
  
- **Missing dependencies**:
  - Run `pip install -r requirements.txt` to ensure all libraries are installed.

- **Performance issues**:
  - Adjust the `chunk_size` in `text_processing.py` or the `similarity_threshold` in `retrieval.py`.

## Future Enhancements

- Add a web-based interface for better usability.
- Extend support for multi-document retrieval.
- Integrate additional language models (e.g., GPT).

## License

This project is licensed under the MIT License.

---
