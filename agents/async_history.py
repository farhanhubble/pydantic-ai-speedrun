import asyncio
import os
from pydantic_ai import Agent


with open("./.secrets/gemini.key", "r") as f:
    google_api_key = f.read().strip()
    os.environ["GOOGLE_API_KEY"] = google_api_key

agent = Agent(
    "google-gla:gemini-2.0-flash-lite",
)


async def main():
    result = await agent.run("Tell me something interesting about the capital of Italy in roughly 140 words?")
    print('\n', result.output)

async def progress():
    print('Thinking ', end='', flush=True)
    while True:
        print('.', end='', flush=True)
        await asyncio.sleep(.1)


async def run_with_progress():
    progress_task = asyncio.create_task(progress())
    await main()
    progress_task.cancel()


if __name__ == "__main__":
    asyncio.run(run_with_progress())
    