import click
import os

from dotenv import load_dotenv
from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.llms.gemini import Gemini

load_dotenv()

def validate_path(ctx, param, value):
    if not os.path.exists(value):
        raise click.BadParameter(
            "Text folder doesn't exist. Create a folder with .txt files in it."
        )
    return value

@click.command()
@click.option(
    "--data_path",
    required=True,
    callback=validate_path,
    help="Path where the text files are located.",
)
def rag(data_path: str):
    Settings.llm = Gemini(
        model="models/gemini-1.5-flash", api_key=os.getenv("GEMINI_API_KEY")
    )
    Settings.embed_model = GeminiEmbedding(
        model_name="models/embedding-001", api_key=os.getenv("GEMINI_API_KEY")
    )

    documents = SimpleDirectoryReader(data_path).load_data()

    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()

    while True:
        query_str = input("Ask anything about the texts (enter to exit):\n")
        if not query_str:
            break
        response = query_engine.query(query_str)

        print(response)


if __name__ == "__main__":
    rag()
