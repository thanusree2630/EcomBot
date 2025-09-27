# 💬 E-commerce chatbot (Gen AI RAG project using LLama and GROQ)

This is POC of an intelligent chatbot tailored for an e-commerce platform, enabling seamless user interactions by accurately identifying the intent behind user queries. It leverages real-time access to the platform's database, allowing it to provide precise and up-to-date responses.

This chatbot currently supports two intents:

- **faq**: Triggered when users ask questions related to the platform's policies or general information. eg. Is online payment available?
- **sql**: Activated when users request product listings or information based on real-time database queries. eg. Show me all nike shoes below Rs. 3000.
- **smalltalk**: support for casual, friendly interaction

## 🛠 Features  
- Clean and responsive **Streamlit-based web interface**  
- Supports multiple query types:  
  - **FAQ Queries** → using RAG for platform-related questions  
  - **SQL Queries** → dynamic product search and filtering  
  - **Small Talk** → casual, friendly interaction  
- Uses **Semantic Routing** to identify user intent intelligently  
- **Fast and accurate responses** powered by **LLaMA-3.3 via GROQ API**  
- **Dynamic product listing** from a local SQLite database (no backend server required)  
- **Modular and well-structured codebase** for quick customization and scaling  

---

## 📂 Project Structure  
```
E_commerce_Chat_Assistant/
│
├── app/                                # Main application logic
│   ├── main.py                         # Streamlit app entry point
│   ├── faq.py                          # FAQ handling (RAG using ChromaDB)
│   ├── sql.py                          # SQL-based product search
│   ├── smalltalk.py                    # Small talk response logic
│   ├── router.py                       # Semantic intent router
│   ├── db.sqlite                       # SQLite database file
│   └── resources/                      # Data files for ingestion
│       ├── faq_data.csv                # Frequently asked questions dataset
│
├── README.md                           # This documentation
└── requirements.txt                    # Python dependencies
```

### Set-up & Execution

1. Run the following command to install all dependencies. 

    ```bash
    pip install -r app/requirements.txt
    ```

1. Inside app folder, create a .env file with your GROQ credentials as follows:
    ```text
    GROQ_MODEL=<Add the model name, e.g. llama-3.3-70b-versatile>
    GROQ_API_KEY=<Add your groq api key here>
    ```

1. Run the streamlit app by running the following command.

    ```bash
    streamlit run app/main.py
    ```

---

## 🧠 How It Works  

### 🔹 Intent Classification (using Semantic Router)  
Each user message is analyzed using the **Semantic Router**.  
The router classifies the query into one of three categories:  
- **faq** → platform policies and general info  
- **sql** → product-related queries using structured data  
- **smalltalk** → casual or generic conversations  

---

### 🔹 Routing Logic  
- **FAQ Route** → Uses **ChromaDB + Sentence Transformers** to retrieve relevant policy answers via semantic search (**RAG**).  
- **SQL Route** → Converts the query into **SQL** using LLMs and executes it on a local **SQLite product database**.  
- **Small Talk** → Returns natural, friendly responses to casual inputs, enhancing engagement.  

---

### 🔹 Dynamic Streamlit Output  
- **SQL Route** → Displays filtered product results with links, titles, and prices.  
- **FAQ Route** → Shows concise and accurate answers sourced from uploaded CSV data.  
- **Small Talk** → Outputs informal, chatbot-style replies for improved UX.  
