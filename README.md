
# LangChain Documentation Helper

A repository for learning LangChain by building a generative ai application.

This is a web application is using a Pinecone as a vectorsotre and answers questions about LangChain 
(sources from LangChain official documentation). 

https://github.com/user-attachments/assets/c0e4eb30-9e01-4e10-a513-61f1d49536a8

## Tech Stack
Client: Streamlit

Server Side: LangChain 🦜🔗

Vectorstore: Pinecone 🌲

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`PINECONE_API_KEY`
`AZUR_OPENAI_API_KEY`

## Run Locally

Clone the project

```bash
  git clone https://github.com/TuyenTrungLe/Documentation-helper
```

Go to the project directory

```bash
  cd Documentation-helper
```

Download LangChain Documentation
```bash
  mkdir langchain-docs
  wget -r -A.html -P langchain-docs  https://api.python.langchain.com/en/latest
```

Install dependencies

```bash
  pipenv install
```

Start the flask server

```bash
  streamlit run main.py
```


## Running Tests

To run tests, run the following command

```bash
  pipenv run pytest .
```


## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/letrungtuyen3101/)
