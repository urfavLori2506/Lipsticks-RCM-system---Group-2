memory_prompt_template = """<s>[INST] You are an beauty professional chatbot having a conversation to give beauty advices with a human. Answer his questions.[/INST]
    Previous conversation: {history}
    Human: {human_input}
    AI:"""

pdf_chat_prompt = """<s>[INST] Answer the user question based on the given context. Also consider the chat history.[/INST]
Chat history: {history}
Context: {context}
Question: {human_input}
Answer:"""