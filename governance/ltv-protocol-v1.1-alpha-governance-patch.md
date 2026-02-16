# LTV Protocol — V1.1-Alpha Governance & Safety Patch

Security, Explainability, Identity, Privacy, and Routing Transparency Extensions

---

## 1. Predict Explainability Surface

To address regulatory, auditability, and agentic decision-trust requirements, the `/predict` endpoint SHALL expose an Explainability Surface.

### Response Fields

- **ltv_value** (float)  
- **confidence** (0–1)

#### feature_attributions (array)
- feature_id (string)
- direction (positive | negative | neutral)
- weight_normalized (0–1)

#### reasoning_path (array)
- category (behavioral | financial | retention | risk)
- summary (string)
- impact_band (low | medium | high)

#### evidence_hashes (object)
- signals_hash (SHA256)
- model_version_hash (SHA256)

**Purpose:**  
Provides audit-grade interpretability without exposing proprietary model parameters.

---

## 2. Identity Trust Chain & Revocation

The `/identity` layer SHALL implement cryptographic trust lifecycle management.

### 2.1 Key Rotation

- jwks_uri endpoint required  
- All signatures MUST include `kid`  
- Parallel key validity supported  

### 2.2 Revocation Endpoints

**Option A — CRL**
```
GET /identity/crl
```

**Option B — Status Check**
```
GET /identity/status?cert_id=
```

### 2.3 Break‑Glass Incident Protocol

Upon key compromise:

1. Immediate `kid` revocation  
2. Incident ID issuance  
3. Routing `safe_mode` activation  
4. TTL cache limit ≤ 5 minutes  

**Purpose:** Rapid containment of trust breaches across agent networks.

---

## 3. Privacy‑Safe Signal Schema

The `PredictRequest.signals` field SHALL move from open schema to strict allowlist validation.

### 3.1 Schema Constraints

Examples of permitted derived signals:

- tenure_days (integer)  
- avg_order_value_180d (float)  
- refund_ratio_90d (float)  
- chargeback_rate_90d (float)  

### 3.2 PII Prohibition

Raw personal data is strictly forbidden, including:

- name  
- email  
- phone  
- wallet balance  

### 3.3 Enforcement Errors

- `PII_DETECTED`  
- `SCHEMA_VIOLATION`  
- `SIGNAL_OUT_OF_RANGE`  

**Purpose:** Ensures GDPR / CCPA compliance and minimizes sensitive data exposure.

---

## 4. Routing Policy Transparency

Routing logic SHALL be governed by versioned, auditable policy artifacts.

### 4.1 Policy Endpoint

```
GET /routing/policy
```

Returns:

- policy_version  
- effective_at  
- change_reason  
- policy_hash (SHA256)  

### 4.2 Transparency Log

Each `policy_hash` SHALL be published to a public transparency log for independent verification.

### 4.3 Multisig Governance

Policy updates REQUIRE M‑of‑N signatures from:

- Protocol operator  
- Independent auditor  
- Industry consortium representative  

**Purpose:** Prevents unilateral routing manipulation and establishes institutional trust.

---

## 5. Positioning Clause

LTV.com provides:

- Canonical schema definitions  
- Transparency logging  
- Reference implementation surfaces  

Root‑of‑trust authority MAY be federated across consortium or public identity infrastructures.

---

**Status:** Draft — Alpha  
**Document Type:** Governance Extension Specification  

---

End of V1.1‑Alpha Governance Patch
