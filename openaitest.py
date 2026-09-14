"""Minimal example of calling the OpenAI Responses API from Python.

Set the OPENAI_API_KEY environment variable before running this example.
"""

from __future__ import annotations

import os

from openai import OpenAI


def main() -> None:
    """Read a prompt, send it to the model, and print the response."""
    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("Set OPENAI_API_KEY before running this example.")

    user_prompt = input("Enter your prompt: ")
    client = OpenAI()
    response = client.responses.create(
        model="gpt-4o-mini",
        instructions="Be strict.",
        input=user_prompt,
    )
    print(response.output_text)


if __name__ == "__main__":
    main()
