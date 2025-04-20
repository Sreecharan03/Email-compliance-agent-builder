import weaviate
from sentence_transformers import SentenceTransformer

client = weaviate.Client("http://localhost:8080")
embedder = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_policy_context(query):
    vector = embedder.encode(query)
    result = client.query.get("EmailPolicyDocs", ["content", "title"]).with_near_vector({"vector": vector.tolist()}).with_limit(1).do()
    try:
        return result["data"]["Get"]["EmailPolicyDocs"][0]["content"]
    except:
        return "No relevant policy found."
