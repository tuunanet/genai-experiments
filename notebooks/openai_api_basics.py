import marimo

__generated_with = "0.17.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from dotenv import load_dotenv, find_dotenv
    from pathlib import Path
    import asyncio
    from openai import OpenAI
    from openai import AsyncOpenAI
    return AsyncOpenAI, OpenAI, Path, asyncio, find_dotenv, load_dotenv, mo


@app.cell
def _(Path, find_dotenv, load_dotenv, mo):
    # Grab the API key from detected .env file and create a client. By default the client checks for OPENAI_API_KEY environment variable.
    path_dotenv_file = Path(find_dotenv())
    load_dotenv(path_dotenv_file, override=True)
    mo.stop()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # OpenAI Responses API

    I noticed a useful [migration guide](https://platform.openai.com/docs/guides/migrate-to-responses) for those more familiar with Chat completions API. Let's try do some basic streaming responses with it.
    """
    )
    return


@app.cell
def _(OpenAI):
    client = OpenAI()

    # If you're using pay-as-you-go tier like me, cold start probably takes 15-20 secs before getting any streamed output
    with client.responses.create(
        model="gpt-5-nano",
        input=[
            {
                "role": "user",
                "content": "Write a riddle consisting of ten sentences.",
            },
        ],
        stream=True,
    ) as stream:
        for event in stream:
            if event.type == "response.output_text.delta":
                # Note: always use flush=True so that text appears in real-time
                print(event.delta, end="", flush=True)
            elif event.type == "response.completed":
                print("\n\n--- Completed streaming")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    # Async chat responses?

    It would be nice to try out async method for OpenAI chat responses, but I do not yet know if I can do that within a Marimo notebook. I will write a potential example here for later reference (or to copy paste and try out in the terminal)
    """
    )
    return


@app.cell
def _(AsyncOpenAI, asyncio):
    client_async = AsyncOpenAI()

    async def main():
        async with client_async.responses.stream(
            model="gpt-5-nano",
            input=[{"role": "user", "content": "Write a riddle consisting of ten sentences."}],
        ) as stream:
            async for event in stream:
                if event.type == "response.output_text.delta":
                    print(event.delta, end="", flush=True)
                elif event.type == "response.completed":
                    print("\n\n--- Completed streaming")

    asyncio.run(main())
    return


if __name__ == "__main__":
    app.run()
