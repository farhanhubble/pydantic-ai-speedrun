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
    async with agent.run_stream("Tell me something interesting about the capital of Italy in roughly 140 words?") as result:
        async for chunk in result.stream_text():
            print(chunk, end='', flush=True)

async def progress():
    print('[Weighing my words...]', flush=True)


async def run_with_progress():
    await asyncio.gather(main(), progress())


if __name__ == "__main__":
    asyncio.run(run_with_progress())
    