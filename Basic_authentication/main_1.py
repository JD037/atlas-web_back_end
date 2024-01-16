#!/usr/bin/env python3
""" Main 1
"""
from api.v1.auth.auth import Auth

a = Auth()

# Print only the results of the method calls
print(a.require_auth(None, ["/api/v1/status/"]))
print(a.require_auth("/api/v1/status/", None))
print(a.require_auth("/api/v1/status/", []))
print(a.require_auth("/api/v1/status/", ["/api/v1/status/"]))
print(a.require_auth("/api/v1/status", ["/api/v1/status/"]))
print(a.require_auth("/api/v1/users", ["/api/v1/status/"]))
print(a.require_auth("/api/v1/users", ["/api/v1/status/", "/api/v1/stats"]))
