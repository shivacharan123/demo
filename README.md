# demo

---

# 🦙 LangChain Chatbot with LLaMA 2 (Streamlit)

This project is a **simple AI chatbot web app** built using **LangChain**, **LLaMA 2 (via Ollama)**, and **Streamlit**.
It allows users to ask questions through a web interface and receive real-time responses from a locally hosted LLM.

---

## 🚀 What This Project Does

* Provides an interactive **chat interface** using Streamlit
* Uses **LangChain prompt templates** to structure conversations
* Runs **LLaMA 2 locally** via Ollama (no external API calls required)
* Supports **LangChain tracing** for debugging and observability

---

## 🧠 How It Works (Brief)

1. **Prompt Template**
   Defines system and user roles using `ChatPromptTemplate`.

2. **LLM Integration**
   Connects to the **LLaMA 2** model running locally through Ollama.

3. **Output Parsing**
   Converts LLM responses into clean text using `StrOutputParser`.

4. **Streamlit UI**

   * Takes user input from a text box
   * Invokes the LangChain pipeline
   * Displays the chatbot response instantly

---

## 🛠️ Tech Stack

* **Python**
* **LangChain**
* **Ollama (LLaMA 2)**
* **Streamlit**
* **dotenv**

---

## ⚙️ Setup & Installation

### 1️⃣ Install Dependencies

```bash
pip install langchain streamlit python-dotenv
```

### 2️⃣ Install and Run Ollama

```bash
ollama run llama2
```

### 3️⃣ Environment Variables

Create a `.env` file:

```env
LANGCHAIN_API_KEY=your_langchain_api_key
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open the browser and start chatting 🚀

---

## 📌 Example Use Cases

* Personal AI assistant
* Local LLM experimentation
* LangChain prompt testing
* Streamlit-based AI demos

---

## 🌟 Why This Project Is Useful

This project demonstrates:

* **End-to-end LangChain pipeline**
* **Local LLM inference with Ollama**
* **Rapid AI app prototyping**
* **Clean separation of prompt, model, and UI**

Perfect for beginners exploring **LangChain + LLM apps**.

