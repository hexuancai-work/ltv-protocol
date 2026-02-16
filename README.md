# LTV Protocol

The LTV Protocol defines a standardized interface surface for value-aware routing and prediction in autonomous commerce systems.

It functions as an interoperable registry layer enabling agents, platforms, and decision systems to reference lifetime value signals through a unified interface.

---

## Canonical Registry

Primary domain anchor:

https://ltv.com

OpenAPI specification:

https://ltv.com/openapi/LTV-v1-OpenAPI.json

---

## Core Endpoints

Base:

https://api.ltv.com

Available primitives:

GET    /identity  
POST   /predict  
GET    /routing?subject=…

These endpoints provide registry identity verification, predictive value outputs, and routing-weight hints for agent decision flows.

---

## Demo

Example agent interaction script:

examples/demo_agent.py

Run locally:

python examples/demo_agent.py

This demonstrates protocol discovery, routing evaluation, and predictive value calls.

---

## Status

Specification: v1.0-alpha  
Registry Node: Mock / Interface-Compatible  
Integration: Agent-Accessible  

Implementation nodes may evolve independently while preserving interface compatibility.

---

## Contact

Registry inquiries:

hello@ltv.com
