# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T09:38:13+00:00



import argparse
import json
import os
from typing import *

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import APIKeyHeader, APIKeyQuery, BaseSecurity

from models import (
    FieldFormatRotoBallerArticlesByDateDateGetResponse,
    FieldFormatRotoBallerArticlesByPlayerIDPlayeridGetResponse,
    FieldFormatRotoBallerArticlesGetResponse,
    Format,
)

app = MCPProxy(
    contact={'x-twitter': 'nfldata'},
    title='MLB v3 RotoBaller Articles',
    version='1.0',
    servers=[
        {'url': 'http://azure-api.sportsdata.io/v3/mlb/articles-rotoballer'},
        {'url': 'https://azure-api.sportsdata.io/v3/mlb/articles-rotoballer'},
    ],
)


@app.get(
    '/{format}/RotoBallerArticles',
    tags=['rotoballer_article_handling'],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def rotoballer_articles(format: Format = 'xml'):
    """
    RotoBaller Articles
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{format}/RotoBallerArticlesByDate/{date}',
    tags=['rotoballer_article_handling'],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def rotoballer_articles_by_date(format: Format = 'xml', date: str = ...):
    """
    RotoBaller Articles By Date
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{format}/RotoBallerArticlesByPlayerID/{playerid}',
    tags=['rotoballer_article_handling'],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def rotoballer_articles_by_player(format: Format = 'xml', playerid: str = ...):
    """
    RotoBaller Articles By Player
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
