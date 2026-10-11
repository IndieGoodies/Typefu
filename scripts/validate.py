#!/usr/bin/env python3
"""Checks every action in actions/ the way Typefu reads it. Uses only the standard library.

Run it from the repository root: python3 scripts/validate.py
"""
import json
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
schema = json.loads((root / "schema.json").read_text())
props = schema["properties"]
errors = []
ids = {}

def fail(path, message):
    errors.append(f"{path.relative_to(root)}: {message}")

for path in sorted((root / "actions").rglob("*")):
    if path.is_dir():
        fail(path, "actions/ has no subfolders; put the file directly in actions/")
        continue
    if path.parent != root / "actions":
        continue
    if path.suffix != ".json":
        fail(path, "only .json files belong in actions/")
        continue
    try:
        action = json.loads(path.read_text(encoding="utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        fail(path, f"not valid JSON: {error}")
        continue
    if not isinstance(action, dict):
        fail(path, "must be a JSON object")
        continue
    for key in schema["required"]:
        if key not in action:
            fail(path, f"missing {key}")
    for key, value in action.items():
        spec = props.get(key)
        if spec is None:
            fail(path, f"unknown key {key}")
            continue
        if "const" in spec and value != spec["const"]:
            fail(path, f"{key} must be {spec['const']}")
        if "enum" in spec and value not in spec["enum"]:
            fail(path, f"{key} must be one of {', '.join(spec['enum'])}")
        if spec.get("type") == "string":
            if not isinstance(value, str) or len(value) < spec.get("minLength", 0):
                fail(path, f"{key} must be a non-empty string")
            elif "maxLength" in spec and len(value) > spec["maxLength"]:
                fail(path, f"{key} is longer than {spec['maxLength']} characters")
            elif "pattern" in spec and not re.fullmatch(spec["pattern"], value):
                fail(path, f"{key} {value!r} doesn't match {spec['pattern']}")
    requirements = action.get("requirements", {})
    if isinstance(requirements, dict):
        allowed = props["requirements"]["properties"]
        for key in requirements:
            if key not in allowed:
                fail(path, f"unknown requirement {key}")
        if requirements.get("regex"):
            try:
                re.compile(requirements["regex"])
            except re.error as error:
                fail(path, f"requirements.regex: {error}")
    else:
        fail(path, "requirements must be an object")
    action_id = action.get("id", "")
    if path.name != f"{action_id}.json":
        fail(path, f"file must be named {action_id}.json")
    if action_id in ids:
        fail(path, f"id {action_id} is also used by {ids[action_id].relative_to(root)}")
    ids[action_id] = path
    if action.get("kind") == "url" and "{text" not in action.get("script", ""):
        fail(path, "URL actions need {text} in the script")

readme = (root / "README.md").read_text(encoding="utf-8")
for action_id, path in ids.items():
    if f"(actions/{action_id}.json)" not in readme:
        fail(path, "add a row for it to the table in README.md")

for error in errors:
    print(error)
print(f"{len(ids)} actions, {len(errors)} problems")
sys.exit(1 if errors else 0)
