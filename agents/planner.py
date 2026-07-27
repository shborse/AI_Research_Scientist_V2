from tools.llm import ask_llm


class PlannerAgent:

    def run(self, topic):

        system_prompt = """
You are an expert AI Research Planner.

Given a research topic, create a detailed research roadmap.

Include:

1. Research Objective

2. Literature Review Tasks

3. Research Gap Tasks

4. Experiment Planning

5. Deliverables

Return markdown.
"""

        return ask_llm(system_prompt, topic)