def only_text(msg) -> str:
    return "".join(b["text"] for b in msg.content_blocks if b["type"] == "text")