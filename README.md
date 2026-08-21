# iet-workshop

Google Agent Development Kit (ADK) workshop environment.

## Setup

```bash
./scripts/install-adk.sh
cp my_agent/.env.example my_agent/.env
# Put a Gemini API key in my_agent/.env
```

The virtualenv is created at `~/.venvs/adk` (not under `/workspace`) so Cloud Agent git checkout cannot delete it.

## Run the Dev UI

From the repository root (the parent of `my_agent/`):

```bash
./scripts/start-adk-web.sh
```

Then open http://127.0.0.1:8000/dev-ui/ (or the forwarded Cloud Agent port).

The starter binds `0.0.0.0:8000` and allows all CORS origins. That is required
in Cursor Cloud: default `adk web` (loopback + loopback-only origins) serves a
black Dev UI when the page is opened through the HTTPS port proxy.

Chat with the sample `my_agent` after selecting it in the UI.
