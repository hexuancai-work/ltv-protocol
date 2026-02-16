import json
import random
import urllib.request
import urllib.parse

BASE = "https://api.ltv.com"


def http_get(path: str):
    req = urllib.request.Request(BASE + path, method="GET")
    with urllib.request.urlopen(req, timeout=10) as r:
        return json.loads(r.read().decode("utf-8"))


def http_post(path: str, payload: dict):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        BASE + path,
        data=data,
        method="POST",
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=10) as r:
        return json.loads(r.read().decode("utf-8"))


class LTVAwareAgent:

    def __init__(self, agent_id):
        self.agent_id = agent_id
        print("\n--- LTV Protocol Demo Agent ---")
        print(f"Agent ID: {self.agent_id}")
        print("Protocol Anchor: https://ltv.com/openapi/LTV-v1-OpenAPI.json\n")

    def check_identity(self):
        print("[identity] Querying registry node...")
        data = http_get("/identity")
        print(json.dumps(data, indent=2))

    def get_routing(self, subject):
        print("\n[routing] Requesting value-weight routing hint...")
        query = urllib.parse.urlencode({"subject": subject})
        data = http_get(f"/routing?{query}")
        print(json.dumps(data, indent=2))
        return data

    def predict_ltv(self):
        print("\n[predict] Requesting LTV prediction...")

        payload = {
            "timeframe_months": 12,
            "sources": ["mock"],
            "signals": {
                "transactions": 42,
                "avg_order_value": 73.5,
                "region": "NA"
            }
        }

        data = http_post("/predict", payload)
        print(json.dumps(data, indent=2))
        return data

    def decision_logic(self, routing_payload):
        weight = routing_payload["value_weight"]
        tier = routing_payload["priority_tier"]

        print("\n[decision] Evaluating routing strategy...")

        if weight > 0.85:
            action = "PRIORITY_ROUTING → High-tier acquisition flow."
        elif weight > 0.5:
            action = "STANDARD_ROUTING → Balanced resource allocation."
        else:
            action = "LOW_PRIORITY → Passive engagement."

        print(f"Priority Tier: {tier}")
        print(f"Execution Strategy: {action}")


if __name__ == "__main__":

    agent = LTVAwareAgent("AGENT-STRAT-01")

    # 1 — Registry Identity
    agent.check_identity()

    # 2 — Simulated Subject Signal
    subject_hash = f"sha256:0x{random.getrandbits(64):016x}"

    routing_data = agent.get_routing(subject_hash)

    # 3 — Predictive Value Call
    agent.predict_ltv()

    # 4 — Decision Layer
    agent.decision_logic(routing_data)
