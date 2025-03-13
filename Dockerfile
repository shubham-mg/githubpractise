FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir streamlit pymongo

EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "profile.py", "--server.port=8501", "--server.address=0.0.0.0"]
