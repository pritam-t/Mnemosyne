from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

client = QdrantClient(host="localhost", port=6333)

encoder = SentenceTransformer("all-MiniLM-L6-v2")
COLLECTION_NAME = "agent_memory"

def retrieve(user_id: str, limit: int = 5):
    query_vector = encoder.encode("user preference").tolist()

    result = client.query_points(
        collection_name=COLLECTION_NAME,
        prefetch=[],
        query=query_vector,
        limit=limit,
        with_payload=True,
    )

    memories = []
    for point in result.points:
        payload = point.payload or {}
        if payload.get("user_id") == user_id:
            memories.append(payload.get("text"))

    return memories
