# /// script
# dependencies = [
#     "mcp[cli]>=1.25.0",
#     "httpx>=0.28.1",
# ]
# ///
from mcp.server.fastmcp import FastMCP
import tools.transit
import tools.issues
import logging

# Initialize FastMCP server
mcp = FastMCP("Winnipeg-311-MCP")

# Register Transit Tools
mcp.tool()(tools.transit.get_bus_arrivals)
mcp.tool()(tools.transit.get_commute_status)
mcp.tool()(tools.transit.find_stops_near)

# Register City/Issue Tools
mcp.tool()(tools.issues.search_311_issues)
mcp.tool()(tools.issues.list_neighborhoods)

if __name__ == "__main__":
    mcp.run()