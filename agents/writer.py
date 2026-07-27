from tools.llm import ask_llm


class WriterAgent:

    def run(self, topic, plan, literature, gaps, experiment, citations):

        system_prompt = """
You are an academic paper writer.

Combine all the information into a professional research report.

Use this structure:

# Abstract

# Introduction

# Literature Review

# Research Gap

# Proposed Experiment

# Conclusion

# References

Return markdown.
"""

        prompt = f"""
Topic:

{topic}

Research Plan:

{plan}

Literature Review:

{literature}

Research Gaps:

{gaps}

Experiment:

{experiment}

References:

{citations}
"""

        return ask_llm(system_prompt, prompt)