from enum import Enum

class ResponseSignal(Enum):
    FILE_UPLOAD_SUCCESS = "file_upload_success"
    FILE_TYPE_NOT_SUPPORTED = "file_type_not_supported"
    FILE_SIZE_EXCEEDED = "file_size_exceeded"
    FILE_IS_VALID = "file_is_valid"
    FILE_UPLOADED_FAILED = "file_uploaded_failed"
    PROCESSING_SUCCESS = "processing_success"
    PROCESSING_FAILED = "processing_failed"
    PROJECT_NOT_FOUND_ERROR = "project_not_found"
    INSERT_INTO_VEXTORDB_SUCCESS = "insert_into_vectordb_success"
    INSERT_INTO_VEXTORDB_ERROR = "insert_into_vectordb_error"
    VECTORDB_COLLECTION_RETRIEVED = "vectordb_collection_retrieved"
    VECTORDB_SEARCH_ERROR = "vectordb_search_error"
    VECTORDB_SEARCH_SUCCESS = "vectordb_search_success"
    RAG_ANSWER_ERROR = "rag_answer_error"
    RAG_ANSWER_SUCCESS = "rag_answer_success"
    NO_FILES_ERROR = "no_files_error"
    