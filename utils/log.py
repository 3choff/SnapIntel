import base64

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def write_log(log_file, chat_history, readable_datetime):
    with open(log_file, "w", encoding="utf-8") as f:
        f.write(f"# SnapIntel\n### Made by [3choff](https://github.com/3choff)\n\n## Session Log of {readable_datetime}\n\n")
    if chat_history:
        with open(log_file, "a", encoding="utf-8") as f:
            for entry in chat_history:
                role = entry.role
                if role == 'user':
                    text = entry.parts[0].text
                    f.write(f"### Question:\n{text}\n")
                    
                    # Check if there's an image in the parts
                    for part in entry.parts:
                        if hasattr(part, 'inline_data') and part.inline_data.mime_type.startswith('image/'):
                            image_data = part.inline_data.data
                            image_base64 = base64.b64encode(image_data).decode('utf-8')
                            image_mime_type = part.inline_data.mime_type
                            f.write(f"\n![Image](data:{image_mime_type};base64,{image_base64})\n\n")
                else:
                    text = entry.parts[0].text
                    f.write(f"### Response:\n{text}\n\n")

def update_log(question, response, log_file, image_path=None):
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"### Question:\n{question}\n")
        if image_path:
            image_base64 = image_to_base64(image_path)
            f.write(f"\n![Image](data:image/jpeg;base64,{image_base64})\n")
        f.write(f"### Response:\n{response}\n\n")