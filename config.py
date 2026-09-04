import os


OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
	raise RuntimeError(
		"OPENROUTER_API_KEY is not set. Configure it as an environment variable."
	)

MODEL_NAME = "meta-llama/llama-3.3-70b-instruct"
# or
# MODEL_NAME = "deepseek/deepseek-chat-v3"