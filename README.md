# FirmFAQ

FirmFAQ is an intelligent chatbot powered by OpenAI's GPT-3.5-turbo model, designed to answer questions about your company using a custom knowledge base. It employs Retrieval-Augmented Generation (RAG) to provide accurate and context-aware responses.

## Features

- **Conversational AI**: Utilizes OpenAI's GPT-3.5-turbo for natural language understanding and generation.
- **Custom Knowledge Base**: Stores company-specific information in a vector database for quick retrieval.
- **Retrieval-Augmented Generation (RAG)**: Enhances AI responses with relevant information from the knowledge base.
- **Streamlit Web Interface**: Provides an easy-to-use chat interface for users.

## OpenAI API Features Used

1. **GPT-3.5-turbo Model**: 
   - Used for generating human-like responses to user queries.
   - Accessed via the `client.chat.completions.create()` method.
   - Example:
     ```python
     chat_completion = client.chat.completions.create(
         messages=messages,
         model="gpt-3.5-turbo",
         temperature=0,
     )
     ```

2. **Text Embeddings (text-embedding-ada-002)**:
   - Used for converting text into vector representations for efficient similarity search.
   - Implemented through ChromaDB's `OpenAIEmbeddingFunction`.
   - Example:
     ```python
     embedding_function = embedding_functions.OpenAIEmbeddingFunction(
         api_key=os.getenv("OPENAI_API_KEY"),
         model_name="text-embedding-ada-002"
     )
     ```

3. **OpenAI Client**:
   - Latest version of the OpenAI Python client is used for API interactions.
   - Initialized with:
     ```python
     from openai import OpenAI
     client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
     ```

4. **Chat Completions API**:
   - Used to generate conversational responses.
   - Supports multi-turn conversations through message history.
   - Allows for system messages to provide context or instructions.

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/bdeva1975/FirmFAQ.git
   cd FirmFAQ
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

4. Populate the knowledge base:
   ```
   python populate_collection.py
   ```

5. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

## Usage

1. Start the Streamlit app as described above.
2. Type your question about the company in the chat input.
3. The AI will respond with relevant information based on the knowledge base and its language understanding capabilities.

## Customization

- Modify `data/company_info.json` to include your company's specific information.
- Adjust the `MAX_MESSAGES` constant in `chatbot_lib.py` to change the conversation history length.
- Experiment with different OpenAI models or parameters in `chatbot_lib.py` to fine-tune the AI's responses.

## Contributing

Contributions to FirmFAQ are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
