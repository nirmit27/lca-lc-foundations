"""
Utility functions
"""

import base64


def img_encoder(img_file):
    """
    Encode an image file to `base64` format for use in multimodal LLM prompts.

    Args:
        img_file: A file object from `st.file_uploader()`, that would be used in the frontend.

    Returns:
        tuple: (base64_encoded_string, mime_type)
    """
    # NOTE: Reset file pointer to the beginning
    img_file.seek(0)
    img_bytes = img_file.read()
    
    img_b64 = base64.b64encode(img_bytes).decode("utf-8")
    filename = img_file.name.lower()

    # NOTE: Detect mime type from file extension.
    if filename.endswith(".png"):
        mime_type = "image/png"
    elif filename.endswith((".jpg", ".jpeg")):
        mime_type = "image/jpeg"
    else:
        mime_type = "image/png"

    return img_b64, mime_type
