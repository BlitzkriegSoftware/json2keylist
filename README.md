# json2keylist

Convert JSON to a list of keys for easy comparison

## Please use UV!

1. Install UV if needed

- See: https://docs.astral.sh/uv/getting-started/installation/

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

1. Create an `.venv`

```powershell
uv venv
```

3. Activate it

```powershell
 .\.venv\Scripts\Activate.ps1
```

## Make sure VSCODE is using correct python

CONTROL+SHIFT+P
`Python: Select Interpreter`
Pick the UV created one.

## How to run from command line

```powershell
uv run main.py {filename}
```

e.g.,

```powershell
uv run main.py .\example\sample01.json
```
