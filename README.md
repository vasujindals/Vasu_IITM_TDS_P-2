# TDS Project 2 – IITM Assignment Solver by Vasu Jindal

This project is a smart assignment-solving API built as part of the **Tools in Data Science** course in the **IIT Madras Online BSc in Data Science** program.

It uses a powerful LLM backend and tool-calling capabilities to handle assignment questions—including those involving ZIP files, CSVs, spreadsheet formulas, PDFs, SQL queries, and more.

> ✨ Developed by **Vasu Jindal**

## 🚀 Quickstart

1. **Clone the repository**
   git clone https://github.com/vasujindals/TDS_Project_2.git
   cd TDS_Project_2

2. **Create a virtual environment**
   python -m venv venv

3. **Activate the virtual environment**
   - Windows:
     venv\Scripts\activate

   - macOS/Linux:
     source venv/bin/activate

4. **Install dependencies**
   pip install -r requirements.txt

5. **Create a `.env` file** and add your AIProxy token:
   AIPROXY_TOKEN=your_token_here

6. **Run the server**
   uvicorn app.main:app --reload


## 📡 API Usage

The API exposes a single endpoint:

**POST** `/api/`

This endpoint accepts:
- `question`: (string) The assignment question
- `file`: (optional) A file such as a `.zip`, `.csv`, `.txt`, etc., if required to answer the question

### 🧪 Sample Request:


curl -X POST "http://localhost:8000/api/" \
  -H "Content-Type: multipart/form-data" \
  -F "question=Download and unzip file abcd.zip. What is the value in the 'answer' column of the CSV file?" \
  -F "file=@abcd.zip"


### ✅ Sample Response:


{
  "answer": "1234567890"
}


---

## 🗂 Project Structure


TDS_Project_2/
│
├── app/
│   ├── main.py               # Main FastAPI app
│   └── utils/
│       ├── file_handler.py   # Utility to handle uploaded files
│       ├── functions.py      # All function-calling tools
│       └── openai_client.py  # Core LLM + tool-call handler
│
├── requirements.txt          # Python dependencies
├── LICENSE                   # MIT License
└── .env                      # Environment variables (not committed)



## 📄 License

This project is licensed under the **MIT License**.  
Feel free to fork, modify, and use it in your own learning journey.



## 🙌 Credits & Context

Originally inspired by the course structure and assignments of **Tools in Data Science (TDS)** from **IIT Madras**, this project takes it a step further by automating the end-to-end solving of typical assignment problems using LLMs and a modular function-calling system.

Built and personalized by [**Vasu Jindal**](https://github.com/vasujindals) ✌️