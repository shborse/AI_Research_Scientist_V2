from tools.llm import ask_llm


class LiteratureAgent:

    def run(self, topic, plan):

        system_prompt = """
You are an expert literature review researcher.

Based on the research plan and topic:

- Summarize current research.
- Mention important discoveries.
- Mention current trends.
- Mention future directions.

Return markdown.
"""

        prompt = f"""
Topic:

{topic}

Research Plan:

{plan}
"""

        return ask_llm(system_prompt, prompt)