import os
from dotenv import load_dotenv
from openai import OpenAI
import chromadb
from chromadb.utils import embedding_functions

# Load environment variables
load_dotenv()

# Set up OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MAX_MESSAGES = 20

class ChatMessage:
    def __init__(self, role, text):
        self.role = role
        self.text = text

def get_collection(path, collection_name):
    embedding_function = embedding_functions.OpenAIEmbeddingFunction(
        api_key=os.getenv("OPENAI_API_KEY"),
        model_name="text-embedding-ada-002"
    )
    
    client = chromadb.PersistentClient(path=path)
    collection = client.get_or_create_collection(collection_name, embedding_function=embedding_function)
    
    return collection

def get_vector_search_results(collection, question):
    results = collection.query(
        query_texts=[question],
        n_results=2
    )
    
    return results

def convert_chat_messages_to_openai_format(chat_messages):
    return [{"role": msg.role, "content": msg.text} for msg in chat_messages]

def process_rag(query, collection):
    search_results = get_vector_search_results(collection, query)
    rag_content = "\n\n".join(search_results['documents'][0])
    
    print("----RAG CONTENT----")
    print(rag_content)
    
    return rag_content

def chat_with_model(message_history, new_text=None):
    collection = get_collection("./data/chroma", "company_info")
    
    new_text_message = ChatMessage('user', text=new_text)
    message_history.append(new_text_message)
    
    if len(message_history) > MAX_MESSAGES:
        del message_history[0:(len(message_history) - MAX_MESSAGES) * 2]
    
    messages = convert_chat_messages_to_openai_format(message_history)
    
    # Get relevant information from the vector database
    rag_content = process_rag(new_text, collection)
    
    # Add the RAG content to the messages
    messages.append({"role": "system", "content": f"Relevant information: {rag_content}\n\nUse this information to answer the user's question if applicable."})
    
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo",
        temperature=0,
    )
    
    output = chat_completion.choices[0].message.content
    
    print("----FINAL RESPONSE----")
    print(output)
    
    response_chat_message = ChatMessage('assistant', output)
    message_history.append(response_chat_message)
    
    return