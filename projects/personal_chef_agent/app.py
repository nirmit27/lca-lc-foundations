"""
Personal Chef - Agent

Powered by **Google Gemini** ✨
"""

from PIL import Image
import streamlit as st

from langchain.messages import HumanMessage

from config import input_modes
from utils import img_encoder
from setup import agent


st.set_page_config(
    page_title="Personal Chef Agent", page_icon="🧑‍🍳", layout="centered"
)

st.title("🧑‍🍳 Personal Chef Agent", text_alignment="center")
st.caption("Powered by Google Gemini ✨", text_alignment="center")

st.divider()

# --- Input Mode ---
st.subheader("Available ingredients ", text_alignment="left")

mode = st.radio("How would you like to provide the ingredients?", input_modes, index=1)

user_input = None
image = None

if mode == "List of ingredients 📝":
    user_input = st.text_area(
        "Enter the list of ingredients that are available to you.",
        placeholder="e.g. eggs, onions, tomatoes, bread, cheese",
        height=120,
    )

else:
    image = st.file_uploader(
        "Upload an image of your fridge or ingredients.", type=["jpg", "jpeg", "png"]
    )

    if image:
        # Encode first, before Image.open() consumes the file pointer
        img_b64, mime_type = img_encoder(image)

        # Now display the image
        img = Image.open(image)
        st.image(img, caption="Uploaded Image", use_container_width=True)

st.divider()

# --- Generate Recipes ---
if st.button("🍽️ Get Recipe Ideas", use_container_width=True):
    if not user_input and not image:
        st.warning("Please provide ingredients or upload an image.")
    else:
        with st.spinner("Searching for delicious recipes... 👨‍🍳"):
            try:
                if user_input:
                    question = HumanMessage(
                        content=[
                            {
                                "type": "text",
                                "text": f"""
                    I have the following ingredients:
                    {user_input}

                    Suggest recipes I can make.
                    """,
                            }
                        ]
                    )
                    response = agent.invoke({"messages": [question]})
                else:
                    multimodal_question = HumanMessage(
                        content=[
                            {
                                "type": "text",
                                "text": "This is what I have left in my refrigerator. What can I make? Give me the detailed recipe instructions.",
                            },
                            {
                                "type": "image",
                                "base64": img_b64,
                                "mime_type": mime_type,
                            },
                        ]
                    )

                    response = agent.invoke({"messages": [multimodal_question]})

                if response is not None:
                    st.success("Here are some ideas! 🍲")
                    st.markdown(response["messages"][-1].content[0]["text"])
                else:
                    st.error("Failed to generate response.")

            except Exception as e:
                st.error("Something went wrong.")
                st.exception(e)
