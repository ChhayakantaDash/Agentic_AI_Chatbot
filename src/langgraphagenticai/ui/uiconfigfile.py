from configparser import ConfigParser #to read configfile uses parser 

class Config:
    def __init__(self,config_file="./src/langgraphagenticai/ui/uiconfigfile.ini"):
        self.config=ConfigParser() #object
        self.config.read(config_file)

    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")
    
    def get_usecase_options(self):
        return [opt.strip() for opt in self.config.get("DEFAULT", "USECASE_OPTIONS").split(",")]

    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(", ")
    
    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")
    