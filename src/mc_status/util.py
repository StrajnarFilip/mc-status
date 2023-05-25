import os

def get_env(environment_variable: str, default: str):
    result = os.getenv(environment_variable)
    return result if result != None else default