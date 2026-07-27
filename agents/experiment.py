from tools.llm import ask_llm


class ExperimentAgent:

    def run(self, topic, gaps):

        system_prompt = """
You are an experienced research scientist.

Design an experiment.

Include:

- Research hypothesis
- Methodology
- Dataset
- Tools
- Evaluation Metrics
- Expected Outcome

Return markdown.
"""

        prompt = f"""
Topic:

{topic}

Research Gaps:

{gaps}
"""

        return ask_llm(system_prompt, prompt)