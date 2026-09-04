from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak

OUTPUT = "PDF_Chatbot_Interview_Guide.pdf"

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    rightMargin=0.65 * inch,
    leftMargin=0.65 * inch,
    topMargin=0.6 * inch,
    bottomMargin=0.6 * inch,
)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="CoverTitle", parent=styles["Title"], alignment=TA_CENTER,
    fontSize=24, leading=29, textColor=colors.HexColor("#17324D"), spaceAfter=14,
))
styles.add(ParagraphStyle(
    name="Subtitle", parent=styles["Normal"], alignment=TA_CENTER,
    fontSize=12, leading=17, textColor=colors.HexColor("#506070"), spaceAfter=26,
))
styles.add(ParagraphStyle(
    name="Section", parent=styles["Heading2"], fontSize=16, leading=20,
    textColor=colors.HexColor("#0B7285"), spaceBefore=14, spaceAfter=7,
))
styles.add(ParagraphStyle(
    name="BodyClean", parent=styles["BodyText"], fontSize=10.2, leading=14,
    spaceAfter=7,
))
styles.add(ParagraphStyle(
    name="Interview", parent=styles["BodyText"], fontSize=10.2, leading=15,
    leftIndent=12, rightIndent=8, borderColor=colors.HexColor("#B7DDE2"),
    borderWidth=0.7, borderPadding=9, backColor=colors.HexColor("#F2FAFA"),
    spaceAfter=10,
))
styles.add(ParagraphStyle(
    name="Small", parent=styles["BodyText"], fontSize=9, leading=12,
    textColor=colors.HexColor("#40505C"),
))


def p(text, style="BodyClean"):
    return Paragraph(text, styles[style])


story = []
story.append(Spacer(1, 0.8 * inch))
story.append(p("AI PDF Chatbot", "CoverTitle"))
story.append(p("Interview Preparation Guide", "Subtitle"))
story.append(p("A practical explanation of the Streamlit, RAG, embeddings, FAISS, and LLM workflow.", "Interview"))
story.append(Spacer(1, 0.35 * inch))
story.append(p("Project Summary", "Section"))
story.append(p(
    "This project is an AI-powered PDF question-answering application. A user uploads a PDF, "
    "the system indexes its contents, and the user can ask questions in natural language. "
    "The application uses Retrieval-Augmented Generation (RAG), so the language model answers "
    "using relevant content retrieved from the uploaded document."
))
story.append(p("One-minute interview answer", "Section"))
story.append(p(
    "I developed a RAG-based PDF chatbot using Python and Streamlit. The application extracts text "
    "from an uploaded PDF, splits it into overlapping chunks, converts the chunks into embeddings "
    "using a Hugging Face model, and stores them in a FAISS vector database. When a user asks a "
    "question, the system retrieves the three most relevant chunks using semantic similarity search. "
    "Those chunks are sent as context to an LLM through OpenRouter, and the model generates the answer. "
    "The API key is loaded from an environment variable instead of being hard-coded."
, "Interview"))
story.append(p("Architecture", "Section"))
architecture = [
    ["Stage", "Implementation", "Purpose"],
    ["Interface", "Streamlit", "PDF upload and question input"],
    ["Extraction", "pypdf", "Read text from each PDF page"],
    ["Chunking", "RecursiveCharacterTextSplitter", "Create searchable text pieces"],
    ["Embeddings", "all-MiniLM-L6-v2", "Represent text meaning as vectors"],
    ["Vector store", "FAISS", "Find similar document chunks quickly"],
    ["Generation", "OpenRouter LLM", "Write a natural-language answer"],
]
table = Table(architecture, colWidths=[1.0 * inch, 2.1 * inch, 3.5 * inch])
table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#17324D")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 9),
    ("LEADING", (0, 0), (-1, -1), 12),
    ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#B8C7D1")),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F3F7F9")]),
    ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ("TOPPADDING", (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
]))
story.append(table)
story.append(p("File responsibilities", "Section"))
story.append(p(
    "<b>app.py:</b> Provides the Streamlit interface and preserves the vector store in session state.<br/>"
    "<b>pdf_reader.py:</b> Uses PdfReader to extract text from every page.<br/>"
    "<b>text_splitter.py:</b> Creates 1,000-character chunks with 200-character overlap.<br/>"
    "<b>vector_store.py:</b> Creates embeddings and stores them in FAISS.<br/>"
    "<b>chatbot.py:</b> Retrieves relevant chunks, builds the prompt, and calls the LLM.<br/>"
    "<b>config.py:</b> Reads the API key from the environment and defines the model name."
))
story.append(PageBreak())
story.append(p("Core Concepts", "Section"))
story.append(p(
    "<b>RAG:</b> Retrieval-Augmented Generation has two steps: retrieve relevant information from the "
    "document, then generate an answer using that information.<br/>"
    "<b>Embeddings:</b> Numerical representations of text meaning. Similar meanings produce nearby vectors.<br/>"
    "<b>Semantic search:</b> Searches by meaning rather than requiring exact keyword matches.<br/>"
    "<b>FAISS:</b> A library for efficient similarity search over vectors.<br/>"
    "<b>Chunk overlap:</b> Shared characters between adjacent chunks preserve context across boundaries."
))
story.append(p("Common interview questions", "Section"))
qa = [
    ("Why use RAG?", "Sending an entire PDF to the model can exceed context limits and increase cost. RAG sends only relevant sections."),
    ("What does k=3 mean?", "The retriever returns the three chunks most similar to the question. This value can be tuned."),
    ("Why use embeddings?", "They enable semantic matching, so related wording can match even when the exact keywords differ."),
    ("Why use Streamlit?", "It provides a fast way to build an interactive Python application without a separate frontend."),
    ("Why use session state?", "Streamlit reruns the script after interactions, so session state preserves the vector store."),
    ("How is the API key protected?", "It is read from OPENROUTER_API_KEY in the environment and local secret files are ignored by Git."),
]
for question, answer in qa:
    story.append(p(f"<b>{question}</b><br/>{answer}"))
story.append(p("Limitations and improvements", "Section"))
story.append(p(
    "Current limitations include no OCR for scanned PDFs, one active document at a time, limited error handling, "
    "and no automatic vector-store loading after restart. Future improvements could add OCR, multiple documents, "
    "chat history, page citations, metadata filtering, reranking, authentication, and API usage limits."
))
story.append(p("Security note", "Section"))
story.append(p(
    "The original API key was exposed in source code. It should be revoked and replaced. The current configuration "
    "expects a new key to be set before running the application.", "Interview"
))
story.append(p("Run command: $env:OPENROUTER_API_KEY=\"your-new-key\"; streamlit run app.py", "Small"))

doc.build(story)
print(f"Created {OUTPUT}")
