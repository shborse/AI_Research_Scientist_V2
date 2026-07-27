from rich.console import Console

from state import ResearchState
from tools.exporter import save_markdown

from agents.planner import PlannerAgent
from agents.literature import LiteratureAgent
from agents.gap import ResearchGapAgent
from agents.experiment import ExperimentAgent
from agents.citation import CitationAgent
from agents.writer import WriterAgent


def main():
    console = Console()

   
    console.print("AI RESEARCH SCIENTIST", style="bold cyan")

    console.print("\nChoose an option:")
    console.print("1. Enter your own research topic")
    console.print("2. Use sample topic")

    choice = input("\nChoice (1/2): ").strip()

    if choice == "2":
        topic = "Applications of Large Language Models in Healthcare"
    else:
        topic = input("\nEnter research topic: ").strip()

    state = ResearchState(topic)

    planner = PlannerAgent()
    literature = LiteratureAgent()
    gap = ResearchGapAgent()
    experiment = ExperimentAgent()
    citation = CitationAgent()
    writer = WriterAgent()

    console.print("\n[cyan]Step 1/6 : Planning research...[/cyan]")
    state.plan = planner.run(state.topic)
    save_markdown("plan.md", state.plan)

    console.print("[green]Step 2/6 : Reviewing literature...[/green]")
    state.literature = literature.run(
        state.topic,
        state.plan
    )
    save_markdown("literature.md", state.literature)

    console.print("[yellow]Step 3/6 : Finding research gaps...[/yellow]")
    state.gaps = gap.run(
        state.topic,
        state.literature
    )
    save_markdown("gaps.md", state.gaps)

    console.print("[blue]Step 4/6 : Designing experiment...[/blue]")
    state.experiment = experiment.run(
        state.topic,
        state.gaps
    )
    save_markdown("experiment.md", state.experiment)

    console.print("[magenta]Step 5/6 : Generating citations...[/magenta]")
    state.citations = citation.run(
        state.topic
    )
    save_markdown("citations.md", state.citations)

    console.print("[bold green]Step 6/6 : Writing final report...[/bold green]")
    state.report = writer.run(
        state.topic,
        state.plan,
        state.literature,
        state.gaps,
        state.experiment,
        state.citations
    )

    console.print("\n" + "=" * 70)
    console.print("[bold green]FINAL RESEARCH REPORT[/bold green]")
    console.print("=" * 70)

    print(state.report)

    approval = input("\nApprove this report? (y/n): ").strip().lower()

    if approval == "y":
        save_markdown("final_report.md", state.report)

        console.print("\n[bold green]✓ Report Approved[/bold green]")
        console.print("[green]Reports saved successfully![/green]")

        console.print("\nGenerated Files:")
        console.print("• reports/plan.md")
        console.print("• reports/literature.md")
        console.print("• reports/gaps.md")
        console.print("• reports/experiment.md")
        console.print("• reports/citations.md")
        console.print("• reports/final_report.md")

    else:
        console.print("\n[bold red]✗ Report Rejected[/bold red]")
        console.print("No final report was saved.")


if __name__ == "__main__":
    main()