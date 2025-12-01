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
    async for event in agent.run_stream_events("Tell me something interesting about the capital of Italy in roughly 140 words?"):
        print(event, flush=True)

async def progress():
    print('[Waiting for events to stream...]', flush=True)


async def run_with_progress():
    await asyncio.gather(main(), progress())


if __name__ == "__main__":
    asyncio.run(run_with_progress())
    