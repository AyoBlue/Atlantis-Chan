import aiohttp
from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport

# Transports

CMS_BRAWLHALLA = AIOHTTPTransport(url="https://cms.brawlhalla.com/graphql")

# GraphQL Queries

PATCH_NOTES = """
query GetPatchNotes($category: String, $after: String, $first: Int = 6) {
    posts(where: {categoryName: $category}, after: $after, first: $first) {
        edges {
            node {
                title
                slug
                dateGmt
                featuredImage {
                    node {
                        sourceUrl
                    }
                }
            }
        }
    }
}
"""

# Async Functions

async def get_patch_notes():
    async with Client(transport=CMS_BRAWLHALLA, fetch_schema_from_transport=False) as session:
        query = gql(PATCH_NOTES)
        result = await session.execute(query, variable_values={"category": "patch-notes", "after": "", "first": 6})

        patch_notes = []
        if result.get("posts") and result["posts"].get("edges"):
            for edge in result["posts"]["edges"]:
                node = edge.get("node")
                if node:
                    patch_notes.append({
                        "title": node.get("title"),
                        "slug": node.get("slug"),
                        "dateGmt": node.get("dateGmt"),
                        "featuredImage": node.get("featuredImage", {}).get("node", {}).get("sourceUrl")
                    })

        return patch_notes

async def get_patch(slug: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://cms.brawlhalla.com/wp-json/wp/v2/posts?slug={slug}") as response:
            if response.status == 200:
                data = await response.json()
                if data:
                    return data[0]

    return None