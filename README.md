# TypeSafe Jev API example

A small command-line example that uses the TypeSafe Python SDK to ask Jev
whether a message expresses urgency. It calls the System One API at
`https://api.typesafe.ai/v1/systemone`.

## Setup

Requires Python 3.10 or newer.

```bash
python -m pip install -r requirements.txt
```

Add your API key to the `.env` file:

```dotenv
TYPESAFE_API_KEY=your-api-key
```

Get an API key from the [TypeSafe console](https://console.typesafe.ai/keys).

## Run

Evaluate the built-in sample message:

```bash
python main.py
```

Or provide your own text:

```bash
python main.py "The deployment is blocked and needs attention immediately."
```

The returned urgency score is a Noul value between `0` and `1`.
