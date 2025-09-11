from rich.console import Console
from rich.panel import Panel
from agents import Agent, Runner, trace  # type: ignore
from research_agents.query_agent import query_agent
from agents import ItemHelpers
from research_agents.query_agent import QueryResponse

console = Console()


class ResearchCoordinator:
    def __init__(self, query: str):
        self.query = query

    async def research(self) -> str:
        with trace("Deep Research Workflow"):
            query_response = await self.generate_queries()
            return "Dummy Report"

    async def generate_queries(self) -> QueryResponse:
        with console.status("[bold cyan]Analyzing Query...[/bold cyan]") as status:

            result = await Runner.run(query_agent, input=self.query)
            console.print(Panel("[bold cyan] Query Analysis [/bold cyan]"))

            console.print("[yellow]Thoughts :[/yellow]", result.final_output.thoughts)
            console.print("[yellow] Genereated Search Queries : [/yellow]")
            for i, query in enumerate(result.final_output.queries):
                console.print(f"{i}-{query}")
            return result.final_output
