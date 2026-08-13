import os



class TemplateParser:
    def __init__(self, language: str = None, default_language: str= "en"):
        self.current_path = os.path.dirname(os.path.abspath(__file__))
        self.default_language = default_language
        self.language = None
        self.set_language(language=language)

    def set_language(self, language: str):

        target = language if language else self.default_language

        if not language:
            self.language = self.default_language
       
        language_path = os.path.join(self.current_path, "locales", language)
        if language and os.path.exists(language_path):
            self.language = language 

        else:
            self.language = self.default_language


    def get(self, group: str, key: str, vars: dict={}):
        if not group or not key:
            return None


        current_lang = self.language or self.default_language
        default_lang = self.default_language or "en"


        group_path = os.path.join(self.current_path, "locales", current_lang, f"{group}.py")
        targeted_language = current_lang


        if not os.path.exists(group_path):
            group_path = os.path.join(self.current_path, "locales",default_lang, f"{group}.py")
            targeted_language = default_lang
            
        if not os.path.exists(group_path):
            return None

        module = __import__(f"stores.llm.templates.locales.{targeted_language}.{group}", fromlist=[group])

        if not module:
            return None

        key_attribute = getattr(module, key)
        return key_attribute.substitute(vars)