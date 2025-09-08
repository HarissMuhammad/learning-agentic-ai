import asyncio
from dotenv import load_dotenv
from rich.console import Console
from rich.prompt import Prompt

load_dotenv()
console = Console()

async def main():
    console.print("[bold blue] Deep Research Agent [/bold blue] - Console Edition")
    console.print("This Tool performs in-depth research on any topic using AI agents.")
    
    #get the users Query
    
    query = Prompt.ask("[bold]What would you like to reasearch[/bold]")
    
    if not query.strip():
        console.print("[red]Error:[/red] Query cannot be empty.")
        return
    
    
if __name__ == "__main__":
    asyncio.run(main())