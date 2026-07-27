from tools.llm import ask_llm


class ResearchGapAgent:

    def run(self, topic, literature):

        system_prompt = """
You are a senior research analyst.

Analyze the literature review and identify:

- Existing limitations
- Research gaps
- Open problems
- Future research opportunities

Return markdown.
"""

        prompt = f"""
Topic:

{topic}

Literature Review:

{literature}
"""

        return ask_llm(system_prompt, prompt)