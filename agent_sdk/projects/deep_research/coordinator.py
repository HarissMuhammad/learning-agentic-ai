from rich.console import Console
from agents import Agent,Runner,trace # type: ignore
from research_agents import query_agent
from research_agents.query_agent import QueryResponse

console = Console()

class ResearchCoordinator:
    def __init__(self, query: str):
        self.query = query
    
    async def research(self):
        with trace("Deep Research Workflow"):
            query_response = await self.generate_queries()
            
    async def generate_queries(self) -> QueryResponse:
        with console.status("[bold cyan]Analyzing Query...[/bold cyan]"):
            
            result = await Runner.run(query_agent,input=self.query)
            console.print("[bold cyan] Query Analysis [/bold cyan]")
            console.print("[yellow]Thoughts :[/yellow]", result.thoughts)
            console.print('[yellow] Genereated Search Queries : [/yellow]')
            for i,query in enumerate(result.queries):
                console.print(f"{i}-{query}")
            
            return result.final_output
