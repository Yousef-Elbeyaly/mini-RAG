from enum import Enum

class ResponseSignal(Enum):
    FILE_UPLOAD_SUCCESS = "file_upload_success"
    FILE_TYPE_NOT_SUPPORTED = "file_type_not_supported"
    FILE_SIZE_EXCEEDED = "file_size_exceeded"
    FILE_IS_VALID = "file_is_valid"
    FILE_UPLOADED_FAILED = "file_uploaded_failed"