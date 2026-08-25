APP_NAME = "mini-RAG"
APP_VERSION = "0.1"
API_KEY = ""


FILE_ALLOWED_TYPES = ["text/plain", "application/pdf"]
FILE_MAX_SIZE = 10
FILE_DEFAULT_CHUNK_SIZE = 512000

POSTGRES_USERNAME="postgres"
POSTGRES_PASSWORD="postgres_password"
POSTGRES_HOST="pgvector"
POSTGRES_PORT=5432
POSTGRES_MAIN_DATABASE="minirag"

#================================ LLM Config ================================
GENERATION_BACKEND = "OPENAI"
EMBEDDING_BACKEND = "OPENAI"

OPENAI_API_KEY = "key__"
OPENAI_API_URL = "url__"
COHERE_API_KEY = "key__"

GENERATION_MODEL_ID_LITERAL = []
GENERATION_MODEL_ID = "id__"
EMBEDDING_MODEL_ID = "id__" 
EMBEDDING_MODEL_SIZE = 

DEFAULT_INPUT_MAX_CHARACTER = 1024
DEFAULT_GENERATION_MAX_OUTPUT_TOKENS = 200
DEFAULT_GENERATION_TEMPERATURE = 0.1

#================================ Vector DB Config ================================
VECTOR_DB_BACKEND_LITERAL = ["QDRANT", "PGVECTOR"]
VECTOR_DB_BACKEND = "PGVECTOR"
VECTOR_DB_PATH = "qdrant_db"
VECTOR_DB_DISTANCE_METHOD = "cosine"
VECTOR_DB_PGVEC_INDEX_THRESHOLD = 500

#================================ Template Configs ================================
PRIMARY_LANG = "ar"
DEFAULT_LANG = "en"
