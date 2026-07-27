# AI Research Scientist

## Overview

AI Research Scientist is a multi-agent AI system that automates the research workflow using Large Language Models. The application coordinates multiple specialized AI agents to generate a research plan, perform a literature review, identify research gaps, design experiments, generate citations, and produce a complete research report.

The project demonstrates agent orchestration, shared state management, and automated report generation using Python and the OpenAI-compatible GitHub Models API.


## Features

- Multi-agent research workflow
- Research planning
- Literature review generation
- Research gap identification
- Experiment design
- Citation generation
- Scientific report writing
- Shared research state across agents
- Markdown report generation
- Human approval before finalizing reports
- Terminal-based interface


## System Architecture

```
                 User
                   │
                   ▼
           Planner Agent
                   │
                   ▼
    Literature Review Agent
                   │
                   ▼
      Research Gap Agent
                   │
                   ▼
    Experiment Design Agent
                   │
                   ▼
        Citation Agent
                   │
                   ▼
    Scientific Writer Agent
                   │
                   ▼
         Human Approval
                   │
                   ▼
     Markdown Report Output
```


## Project Structure

```
AI_Research_Scientist_V2
│
├── agents
│   ├── planner.py
│   ├── literature.py
│   ├── gap.py
│   ├── experiment.py
│   ├── citation.py
│   └── writer.py
│
├── reports
│   ├── plan.md
│   ├── literature.md
│   ├── gaps.md
│   ├── experiment.md
│   ├── citations.md
│   └── final_report.md
│
├── tools
│   ├── exporter.py
│   └── llm.py
│
├── config.py
├── memory.py
├── state.py
├── main.py
├── requirements.txt
├── .env.example
└── README.md
```


## Technology Stack

- Python 3.12
- OpenAI Python SDK
- GitHub Models API
- Rich
- python-dotenv


## Installation

Clone the repository.

```bash
git clone https://github.com/shborse/AI_Research_Scientist_V2.git
```

Navigate to the project directory.

```bash
cd AI_Research_Scientist_V2
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate the environment.

Windows

```bash
.venv\Scripts\activate
```

Linux/macOS

```bash
source .venv/bin/activate
```

Install the required packages.

```bash
pip install -r requirements.txt
```


## Environment Variables

Create a `.env` file in the project directory.

```env
OPENAI_API_KEY=your_github_models_token
OPENAI_BASE_URL=https://models.github.ai/inference
MODEL_NAME=openai/gpt-4.1
```


## Running the Application

Run the application using:

```bash
python main.py
```

The application allows the user to:

- Enter a custom research topic
- Use a predefined sample topic

The complete research workflow is executed automatically.


## Workflow

### Planner Agent

Creates a structured research roadmap.

### Literature Review Agent

Summarizes existing research, important findings, and current trends.

### Research Gap Agent

Identifies limitations, unanswered questions, and future research opportunities.

### Experiment Design Agent

Designs an experimental methodology, datasets, evaluation metrics, and expected outcomes.

### Citation Agent

Generates references in APA format.

### Scientific Writer Agent

Combines outputs from all previous agents into a complete research report.


## Generated Output

After successful execution, the following files are generated inside the `reports` directory.

```
reports/
├── plan.md
├── literature.md
├── gaps.md
├── experiment.md
├── citations.md
└── final_report.md
```


## Example Research Topics

- Applications of Large Language Models in Healthcare
- Explainable Artificial Intelligence
- Autonomous Vehicles
- Smart Agriculture
- AI in Medical Diagnosis
- Climate Change Prediction
- Quantum Machine Learning


## Future Enhancements

- PDF report generation
- Web-based user interface
- Integration with Semantic Scholar
- Integration with arXiv
- Persistent research history
- Improved citation validation
- Multi-user support


## Author

Shreya Borse

GitHub: https://github.com/shborse

---

## License

This project is developed for educational and learning purposes.
