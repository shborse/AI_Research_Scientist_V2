from tools.llm import ask_llm


class CitationAgent:

    def run(self, topic):

        system_prompt = """
Generate 10 realistic academic references related to the topic.

Return APA format.

Do not invent obviously fake journals.
"""

        return ask_llm(system_prompt, topic)