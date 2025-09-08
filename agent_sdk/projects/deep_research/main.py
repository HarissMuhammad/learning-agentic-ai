import asyncio
from dotenv import load_dotenv
from rich.console import Console

async def main():
    print("env initiated")
    load_dotenv()
    console = Console()

if __name__ == "__main__":
    asyncio.run(main())