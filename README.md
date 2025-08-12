# AI-Productivity-Booster 🚀
Supercharge your workflow with an intelligent AI assistant that automates tasks and provides instant, real-time insights. The **AI-Productivity-Booster** is a web-based agent designed to save you time and help you work smarter, not harder.

Key Features ✨
  * **Intelligent AI Agent:** Powered by the **Google Gemini Pro** model to understand and respond to complex queries. 🤖
  * **Real-Time Web Search:** Integrates **DuckDuckGo Tools** to fetch up-to-date information directly from the web. 🔍
  * **Intuitive UI:** Built with **Streamlit** for a clean, interactive, and user-friendly experience. 💻
  * **Task Automation:** Streamline your research and information-gathering tasks with a simple text prompt. ⚡️

How to Run Locally 💻
1.  Clone the repository:
    ```bash
    git clone https://github.com/aditiverma29/Ai-Productivity-Booster.git
    cd Ai-Productivity-Booster
    ```
    
2.  Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3.  Activate the environment:
      * **On Windows:** `venv\Scripts\activate`
      * **On macOS/Linux:** `source venv/bin/activate`

4.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5.  Set up API key:
      * Create a file named `.env` in the project's root directory.
      * Add your Google Gemini API key to the file. You can get a key from [Google AI Studio](https://aistudio.google.com/app/apikey).
      * The file should look like this:
        ```
        GOOGLE_API_KEY="your_api_key_here"
        ```

6.  Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

    Your app will now open in your web browser.

Technologies Used 🛠️

  * **Python**
  * **Streamlit**
  * **Google Gemini Pro**
  * **`python-dotenv`**
  * **`agno` library**
