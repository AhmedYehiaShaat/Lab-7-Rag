# Simple RAG Lab

Simple lab sequence:

```text
01_documents.py
02_preprocessing.py
03_chunking.py
04_vector_representation.py
05_create_chroma_store.py
06_retrieve_context.py
07_prompting.py
streamlit_app.py
```

Final retrieval:

```text
hybrid = 0.4 * BM25 + 0.6 * all-MiniLM-L6-v2 embeddings
```

Run manually:

```powershell
python -m pip install -r requirements.txt
Copy-Item .env.example .env
python 05_create_chroma_store.py
streamlit run streamlit_app.py
```
