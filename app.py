from flask import Flask
import strawberry
from strawberry import Schema
from strawberry.flask.views import GraphQLView
from typing import Annotated, List

from fastmcp import FastMCP
from flask_cors import CORS

app = Flask(__name__)
mcp = FastMCP(name = 'graphql_example')
CORS(app)

# define the return object type and description
@strawberry.type
class ReturnString:
	greeting: str = strawberry.field(
		description="a greeting returned using the name passed in from the query"
		)

# Define GraphQL schema
@strawberry.type
class Query:
    @strawberry.field
    def resolve_hello(self, info, 
		name: Annotated[str,
		strawberry.argument(description="an optional name to provide for the response")
		] = 'stranger') -> ReturnString:
	    return ReturnString(greeting = f"Hello {name}!")

schema = Schema(query=Query)


@mcp.tool(
    description="GraphQL endpoint for querying data using GraphQL expecting POST requests to /graphql with a JSON body containing the query",
    name="GraphQL Endpoint",
)
@app.route('/graphql', methods=['GET', 'POST'])
def graphql():
    view = GraphQLView.as_view('graphql', schema=schema, graphiql=True)
    return view()

@mcp.tool(
    description="Get information about the GraphQL schema in string format for use in constructing queries",
)
@app.route('/schema_info', methods=['GET'])
def schema_info():
    return str(schema)

@mcp.tool(
    description=f"a simple tool for the LLM to use for running queries against the GraphQL endpoint, Graphql Schema is as follows: {str(schema)}",
    name="Run GraphQL Query" 
)
def run_query(query_string: str) -> str:
    # take the incoming query string and execute it against the schema
    query = strawberry.graphql.parse(query_string)
    result = schema.execute_sync(query)
    if result.errors:
        return f"Errors: {result.errors}"
    return str(result.data)

if __name__ == '__main__':
    app.run(debug=True)
