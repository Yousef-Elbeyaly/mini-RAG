from enum import Enum

class LLMEnums(Enum):

    OPEN_AI = "OPEN_AI"
    COHERE = "COHERE"

class OpenAIEnum(Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"