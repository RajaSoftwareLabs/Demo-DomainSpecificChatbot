from langchain import PromptTemplate


class PromptGeneration():
    """Generate prompts for different scenarios."""
    
    def generate_prompt(self, prev_conversations: str) -> PromptTemplate:
        """Returns prompt template based on availability of previous conversation."""

        if (prev_conversations and prev_conversations.strip()):
            return self.__qa_prompt_with_previous_conv()
        else:
            return self.__qa_prompt_without_previous_conv()

    def __qa_prompt_with_previous_conv(self) -> PromptTemplate:
        """Returns prompt template when previous conversation is available."""

        prompt_text = """Act as a smart assistant in a hospital. Use the following pieces of CONTEXT, PREVIOUS_CONVERSATION to answer the user's QUESTION related to the hospital environment. If you don't know the answer, just say that you don't know, don't try to make up an answer.

    CONTEXT: ```{context}```

    PREVIOUS_CONVERSATION: ```{previous_conversation}```

    QUESTION: {question}

    It is very IMPORTANT that after providing a complete answer for the QUESTION, you also need to provide JSON with a "summary" key containing a very short summary of your answer and a "question" key containing the asked QUESTION.
    """

        prompt_template = PromptTemplate(template=prompt_text, input_variables=[
                                         "context", "question", "previous_conversation"])
        return prompt_template

    def __qa_prompt_without_previous_conv(self) -> PromptTemplate:
        """Provides a prompt template in the absence of a previous conversation.
        Utilize this when initiating a conversation for the first time with no 
        prior interactions.
        """

        prompt_text = """Act as a smart assistant in a hospital. Use the following pieces of CONTEXT to answer the user's QUESTION related to the hospital environment. If you don't know the answer, just say that you don't know, don't try to make up an answer.

    CONTEXT: ```{context}```

    QUESTION: {question}

    It is very IMPORTANT that after providing a complete answer for the QUESTION, you also need to provide JSON with a "summary" key containing a very short summary of your answer and a "question" key containing the asked QUESTION.
    """

        prompt_template = PromptTemplate(
            template=prompt_text, input_variables=["context", "question"])
        return prompt_template
