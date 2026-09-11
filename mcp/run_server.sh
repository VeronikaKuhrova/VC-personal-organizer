#!/bin/bash

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"

exec "$PROJECT_DIR/.venv-mcp/bin/python" "$PROJECT_DIR/mcp/server.py"