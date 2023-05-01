# [step 1]>> 
API_KEY = "sk-SW@163.com"    

# [step 2]>> 
USE_PROXY = True
if USE_PROXY:
    proxies = {"http":  "socks5h://localhost:443"}

# [step 3]>> 
DEFAULT_WORKER_NUM = 3


# [step 4]>> 
CHATBOT_HEIGHT = 1115

CODE_HIGHLIGHT = True

LAYOUT = "LEFT-RIGHT"  
DARK_MODE = True  

TIMEOUT_SECONDS = 30

WEB_PORT = -1

MAX_RETRY = 2


LLM_MODEL = "api2d-gpt-3.5-turbo" 
AVAIL_LLM_MODELS = ["gpt-3.5-turbo", "api2d-gpt-3.5-turbo", "gpt-4", "api2d-gpt-4", "chatglm", "newbing"]


LOCAL_MODEL_DEVICE = "cpu" # 可选 "cuda"


CONCURRENT_COUNT = 100

# 设置用户名和密码（不需要修改）（相关功能不稳定，与gradio版本和网络都相关，如果本地使用不建议加这个）
# [("username", "password"), ("username2", "password2"), ...]
AUTHENTICATION = []

# 重新URL重新定向，实现更换API_URL的作用（常规情况下，不要修改!!）
# （高危设置！通过修改此设置，您将把您的API-KEY和对话隐私完全暴露给您设定的中间人！）
# 格式 {"https://api.openai.com/v1/chat/completions": "在这里填写重定向的api.openai.com的URL"} 
# 例如 API_URL_REDIRECT = {"https://api.openai.com/v1/chat/completions": "https://ai.open.com/api/conversation"}
API_URL_REDIRECT = {}

# 如果需要在二级路径下运行（常规情况下，不要修改!!）（需要配合修改main.py才能生效!）
CUSTOM_PATH = "/"

# 如果需要使用newbing，把newbing的长长的cookie放到这里
NEWBING_STYLE = "creative"  # ["creative", "balanced", "precise"]
NEWBING_COOKIES = """
your bing cookies here
"""