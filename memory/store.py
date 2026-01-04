from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from sentence_transformers import SentenceTransformer
import uuid

# Embedding model (must match vector size in Qdrant)
encoder = SentenceTransformer("all-MiniLM-L6-v2")

client = QdrantClient(host="localhost", port=6333)

COLLECTION_NAME = "agent_memory"

def store_memory(user_id: str, text: str):
    vector = encoder.encode(text).tolist()

    point = PointStruct(
        id=str(uuid.uuid4()),
        vector=vector,
        payload={
            "user_id": user_id,
            "text": text
        }
    )

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=[point]
    )
