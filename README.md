Here's a detailed **README** for your project:

---

# **Phi Playground Application**

This project demonstrates the use of the `phi` library to create a playground application with two AI agents: a web search agent and a financial agent. These agents leverage Groq models and specific tools to perform their respective tasks, providing interactive and intelligent functionalities.

## **Features**
- **Web Search Agent**: 
  - Uses DuckDuckGo for searching the web.
  - Includes sources in the responses.
  - Supports Markdown formatting.
  
- **Financial Agent**:
  - Fetches financial data using YFinanceTools, including:
    - Stock prices.
    - Analyst recommendations.
    - Stock fundamentals.
    - Company news.
  - Displays data in tables and Markdown.

## **Installation**

### **Prerequisites**
- Python 3.8+
- Required libraries (`phi`, `openai`, `dotenv`, etc.)
- API keys for `Groq` and `Phi`.

### **Setup**
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory with the following content:
   ```plaintext
   GROQ_API_KEY=<your_groq_api_key>
   PHI_API_KEY=<your_phi_api_key>
   ```

## **Usage**

1. Start the application:
   ```bash
   python app.py
   ```

2. Access the application in your web browser. By default, it should be available at `http://127.0.0.1:8000`.

3. Interact with the agents:
   - **Web Search Agent**: Provide a query, and it will return results with sources.
   - **Financial Agent**: Request financial data, and it will present results in a tabular format.

## **Project Structure**
```
.
├── app.py                # Main application file
├── requirements.txt      # List of dependencies
├── .env                  # Environment variables (not included in the repository)
└── README.md             # Project documentation
```

## **Dependencies**
- `phi`
- `openai`
- `dotenv`
- `yfinance`
- `duckduckgo`

Install all dependencies using:
```bash
pip install -r requirements.txt
```

## **Contributing**
1. Fork the repository.
2. Create a new feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature description"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

## **License**
This project is licensed under the MIT License. See the LICENSE file for details.

## **Acknowledgments**
- `phi` library for providing tools and models.
- DuckDuckGo for web search functionalities.
- YFinance for financial data.

---

You can modify this **README** further to suit your specific repository and project needs.