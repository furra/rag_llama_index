import click
import os

from dotenv import load_dotenv
from llama_index.core import Settings, SQLDatabase
from llama_index.core.query_engine import NLSQLTableQueryEngine
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.llms.gemini import Gemini
from sqlalchemy import create_engine

load_dotenv()


@click.command()
@click.option(
    "--db_file",
    required=True,
    help="Path to the database file.",
)
def rag(db_file: str):
    Settings.llm = Gemini(
        model="models/gemini-1.5-flash", api_key=os.getenv("GEMINI_API_KEY")
    )
    Settings.embed_model = GeminiEmbedding(
        model_name="models/embedding-001", api_key=os.getenv("GEMINI_API_KEY")
    )

    engine = create_engine(f"sqlite:///{db_file}")

    sql_database = SQLDatabase(engine, include_tables=["purchases"])

    query_engine = NLSQLTableQueryEngine(
        llm=Settings.llm,
        sql_database=sql_database,
        tables=["purchases"],
    )

    while True:
        query_str = input("Ask anything about the data (CTRL+d to exit):\n")
        if not query_str:
            break
        response = query_engine.query(query_str)

        print(response)


if __name__ == "__main__":
    rag()
