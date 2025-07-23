from langchain.chains import LLMChain, SequentialChain
from langchain.prompts import PromptTemplate
from langchain.llms import Gemini
import os

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

gemini_llm = Gemini(api_key=GEMINI_API_KEY)

# Prompt for summarization
summarize_prompt = PromptTemplate(
    input_variables=["article_text"],
    template="""
Summarize the following news article in 3-5 sentences:

{article_text}
"""
)

# Prompt for topic classification
classify_prompt = PromptTemplate(
    input_variables=["summary"],
    template="""
Classify the topic of this news summary as one of: financial, politics, technology, sports, entertainment, science, other.
Summary:
{summary}
Topic:
"""
)

# Prompt for language detection
language_prompt = PromptTemplate(
    input_variables=["summary"],
    template="""
Detect the language of this news summary:
Summary:
{summary}
Language:
"""
)

# Chains
summarize_chain = LLMChain(llm=gemini_llm, prompt=summarize_prompt, output_key="summary")
classify_chain = LLMChain(llm=gemini_llm, prompt=classify_prompt, output_key="topic")
language_chain = LLMChain(llm=gemini_llm, prompt=language_prompt, output_key="language")

summarizer_chain = SequentialChain(
    chains=[summarize_chain, classify_chain, language_chain],
    input_variables=["article_text"],
    output_variables=["summary", "topic", "language"],
    verbose=True,
)

def summarize_article(article_text: str):
    """Summarize, classify topic, and detect language of an article using Gemini via LangChain."""
    return summarizer_chain({"article_text": article_text})
