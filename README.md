I used VS Code for building this project below are the steps to follow for VS Code editor
In my case I have created a virtual environment "llm_env" and installed all the dependencies there.

1. Go to terminal in VS code 
2. Select command prompt instead of powershell 
3. Check the virtual environment it should show "(llm_env) C:\Users\ADMIN>" because this is the environment created for llm
4. Change the path to the existing app folder "(llm_env) C:\Users\ADMIN>cd C:\Users\ADMIN\OneDrive\Documents\LLM "
5. Run the streamlit "(llm_env) C:\Users\ADMIN\OneDrive\Documents\LLM> streamlit run restaurant_streamlit_app.py "
6. It should open the browser window with streamlit.
7. If any changes save it and rerun it in the streamlit tab of your browser.

"""
import os
from secret_key import gemini_secretKey
os.environ['GOOGLE_API_KEY'] = gemini_secretKey 
"""
I have created a secret_key.py file which has gemini api, you have replace it with your own key.
