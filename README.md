# DomainSpecificChatbot
This is an implementation of a Domain-specific Chatbot powered by GPT models. The chatbot is created with Retrieval Augmented Generation (RAG) technique.

The Chatbot implementation includes functionalities such as diverse data handling, embedding generation, storage of embeddings in FAISS (a vector store), creating dynamic prompts, integrating with MongoDB to store user conversations, provision of an accessible API endpoint for integration with mobile and web apps, and integrating with the OpenAI Chat Completion API. Additionally, it has few files containing mock hospital data and a requirements file listing all necessary libraries for running this project.

# Pre-requisites
Since the entire project is in Python, you need to have [python](https://wiki.python.org/moin/BeginnersGuide/Download), [pip](https://pip.pypa.io/en/stable/installation/), and [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) libraries installed. Additionally, to run the Chatbot, make sure you have the following:
1. Install the necessary libraries for the chatbot listed in the [requirements](https://github.com/RajaSoftwareLabs/Demo-DomainSpecificChatbot/blob/main/requirements.txt) file by running the command `pip install -r requirements.txt`.
2. Obtain an OpenAI API key (as mentioned [here](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key)) and store it in the [environment](https://github.com/RajaSoftwareLabs/Demo-DomainSpecificChatbot/blob/main/.env) file.
3. Get a MongoDB connection string (as mentioned [here](https://www.mongodb.com/basics/mongodb-connection-string#:~:text=How%20to%20get%20your%20MongoDB%20Atlas%20connection%20string)) and use it in the [manage conversations](https://github.com/RajaSoftwareLabs/Demo-DomainSpecificChatbot/blob/d0e6585d9961f7e608a6fda742a9cbec09919b43/manage_conversations.py#L9) file.

After that, run the local server by invoking [server.py](https://github.com/RajaSoftwareLabs/Demo-DomainSpecificChatbot/blob/main/server.py) and access the ["/chat"](https://github.com/RajaSoftwareLabs/Demo-DomainSpecificChatbot/blob/d0e6585d9961f7e608a6fda742a9cbec09919b43/server.py#L25-L28) API endpoint from mobile/web apps to start chatting.

# Chatbot in Action
Following GIF demonstrates the Chatbot's functionality when the API endpoint is hit with user query and userId.

![alt text](https://github.com/rsl-jainishchampaneria/QA-OpenAI-langchain-custom-data/assets/138757720/55850b28-846c-43c5-a5f6-f1e0e56a7be2 "Chatbot in action")

The GIF below provides a glimpse into the action that happens behind the scenes.

![alt text](https://github.com/rsl-jainishchampaneria/QA-OpenAI-langchain-custom-data/assets/138757720/18c82068-18f2-4869-8717-b9ad47704975 "BTS Chatbot")

# RAG Architecture (used for the Chatbot)
The RAG (Retrieval Augmented Generation) technique combines an LLM (Large Language Model) with an Information Retrieval (IR) system. The LLM is responsible for generating text, while the IR system retrieves relevant information from a knowledge base. Essentially, it retrieves relevant information from a large dataset based on a user query and then encapsulates this information with the query in a prompt, serving as an instruction for the LLM to generate a response accordingly.

![alt text](https://github.com/rsl-jainishchampaneria/QA-OpenAI-langchain-custom-data/assets/138757720/77ed5aa8-7d12-4a1b-98fb-be4cb5321d1b "RAG Architecture")

# Note
This code/software is NOT licensed and is not open for use/change/distribution. Please open an issue / pull-request if you require the same.
