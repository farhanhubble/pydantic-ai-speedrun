from argparse import ArgumentParser
from pydantic_ai import Agent, RunContext

agent = Agent(
    "google-gla:gemini-2.0-flash-lite",
    deps_type=int,
    output_type=bool,
    system_prompt="""
    Use the `roulette_wheel` function to see if the 
    customer has won based on the number they provide.
    """,
)


@agent.tool
async def roulette_wheel(ctx: RunContext[int], square: int) -> str:  
    """check if the square is a winner"""
    return 'winner' if square == ctx.deps else 'loser'


SECRET_NUMBER = 17

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "bet_text",
        type=str,
        required=True,
        help="A natural language description of the bet",
    )
    args = parser.parse_args()

    result = agent.run_sync(str(args.bet_text), deps=SECRET_NUMBER)
    print(result.output)