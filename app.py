from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
import strawberry
from strawberry_permissions import GraphQLContext
from strawberry_types import QueryType

app = FastAPI()


async def get_context() -> GraphQLContext:
    """Get context for the GraphQL API.

    Returns:
        GraphQLContext: The GraphQl Context
    """
    return GraphQLContext()


@strawberry.type
class Query(QueryType):
    """_summary_
    Query class defines the root query fields for the GraphQL schema.
    """

    pass


@app.post("/schema")
async def root():
    with open("schema.graphql", "w", encoding="utf-8") as f:
        f.write(schema.as_str())
        return {"message": schema.as_str()}


schema = strawberry.Schema(query=Query)


gql_app = GraphQLRouter(schema, path="/graphql", debug=True, context_getter=get_context)

app.include_router(gql_app)
