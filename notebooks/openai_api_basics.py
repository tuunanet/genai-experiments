import marimo

__generated_with = "0.17.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from dotenv import load_dotenv, find_dotenv
    from pathlib import Path
    from openai import OpenAI
    return OpenAI, Path, find_dotenv, load_dotenv, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# OpenAI client instance""")
    return


@app.cell
def _(OpenAI, Path, find_dotenv, load_dotenv):
    # Grab the API key from detected .env file and create a client. By default the client checks for OPENAI_API_KEY environment variable.
    path_dotenv_file = Path(find_dotenv())
    load_dotenv(path_dotenv_file, override=True)
    client = OpenAI()
    return (client,)


@app.cell
def _(client):
    # Let's see what models we've got
    for model in client.models.list():
        print(model)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # OpenAI Completion vs. Responses API

    I noticed many online courses have been made before responses API has become available, but fortunately OpenAI provides a [migration guide](https://platform.openai.com/docs/guides/migrate-to-responses) we can refer to when still seeing code using the old Chat completions API.
    """
    )
    return


@app.cell
def _(client):
    # Invoke an output response with the instance of the initialized responses client.
    response = client.responses.create(
        model="gpt-5-nano",
        input="Write a short bedtime story about a unicorn."
    )

    print(response.output_text)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
