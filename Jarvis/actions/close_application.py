"""Close a running desktop program by name. Never opens a browser."""

from actions.computer_settings import close_app, _extract_close_target

_SELF_NAMES = {
    "jarvis", "yourself", "you", "the assistant", "assistant",
    "the hud", "hud", "mark", "mark liii",
}

# If the user said "close X", these tools must not run — they Alt+F4, Google,
# or open Chrome instead of closing the named program.
_HIJACK_TOOLS = {
    "web_search", "browser_control", "open_app", "computer_control",
    "desktop_control", "shutdown_jarvis", "youtube_video",
    "computer_settings",
}


def maybe_reroute_close(utterance: str, tool_name: str, args: dict | None) -> str | None:
    """If the user asked to close a named app, do that and skip the other tool."""
    name = _extract_close_target(utterance or "")
    if not name or name.lower() in _SELF_NAMES:
        return None
    if tool_name == "close_application":
        args = args or {}
        if not str(args.get("name") or args.get("target") or "").strip():
            args["name"] = name
        return None
    if tool_name in _HIJACK_TOOLS:
        return close_app(name)
    return None


def close_application(
    parameters: dict = None,
    player=None,
    session_memory=None,
) -> str:
    params = parameters or {}
    name = str(
        params.get("name")
        or params.get("target")
        or params.get("app")
        or params.get("app_name")
        or ""
    ).strip()
    if not name:
        spoken = str(params.get("utterance") or params.get("description") or "").strip()
        extracted = _extract_close_target(spoken) if spoken else None
        if extracted:
            name = extracted
        elif spoken:
            name = spoken
    if not name:
        return (
            "Which program should I close? Name it — for example "
            "'close Arma Reforger' or 'close Chrome'."
        )
    if player:
        try:
            player.write_log(f"[Close] {name}")
        except Exception:
            pass
    return close_app(name)


TOOL = {
    "name": "close_application",
    "description": (
        "THE ONLY tool for closing, quitting, exiting, or killing a program that "
        "is ALREADY RUNNING on this computer — games, Discord, Steam, Chrome, "
        "Arma Reforger, etc. "
        "Call this immediately when the user says close/quit/exit/kill + a name. "
        "Pass their spoken name even if it is misspelled (amor reforger = Arma Reforger). "
        "NEVER use web_search, browser_control, or open_app for this. "
        "NEVER open Chrome. NEVER look the name up on Google. "
        "NEVER call shutdown_jarvis unless they want to quit Jarvis itself."
    ),
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "name": {
                "type": "STRING",
                "description": (
                    "App or window to close, as spoken "
                    "(e.g. 'Arma Reforger', 'amor reforger', 'Chrome', 'Discord')"
                ),
            },
        },
        "required": ["name"],
    },
    "handler": close_application,
}
