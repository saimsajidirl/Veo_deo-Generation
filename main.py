import streamlit as st
import time
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("GOOGLE_API_KEY not found in .env file.")
    st.stop()
os.environ["GOOGLE_API_KEY"] = api_key

st.title("Veo AI Video Generator")

model_option = st.selectbox("Select Veo Model:", ["veo-2", "veo-3"], index=0)

prompt = st.text_area("Enter your video prompt:")

if st.button("Generate Video") and prompt:
    st.info("Generating video, please wait. This may take a minute...")
    client = genai.Client()
    try:
        model_name = "veo-2.0-generate-001" if model_option == "veo-2" else "veo-3.0-generate-001"
        operation = client.models.generate_videos(
            model=model_name,
            prompt=prompt,
            config=types.GenerateVideosConfig(
                person_generation="dont_allow",
                aspect_ratio="16:9",
                number_of_videos=1
            ),
        )
        while not operation.done:
            time.sleep(20)
            operation = client.operations.get(operation)
        generated_video = operation.response.generated_videos[0] if operation.response and hasattr(operation.response, 'generated_videos') else None
        if not generated_video or not hasattr(generated_video, 'video'):
            st.error("No video was generated. Please try again or check your prompt/model selection.")
        else:
            video_file = generated_video.video
            temp_video_path = f"video_{int(time.time())}.mp4"
            client.files.download(file=video_file)
            if hasattr(video_file, 'save'):
                video_file.save(temp_video_path)
                st.success("Video generated!")
                with open(temp_video_path, "rb") as f:
                    st.video(f.read())
                    st.download_button("Download Video", f, file_name=temp_video_path)
                os.remove(temp_video_path)
            else:
                st.error("Failed to save the generated video file.")
    except Exception as e:
        st.error(f"Error: {e}") 