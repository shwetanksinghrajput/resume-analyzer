# 1. Use an official Python runtime
FROM python:3.9-slim

# 2. Set the directory inside the container
WORKDIR /app

# 3. Install system dependencies (needed for Spacy and image handling)
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# 4. Copy everything from your repo into the container
COPY . .

# 5. Install your 84+ Python packages
RUN pip install --no-cache-dir -r requirements.txt

# 6. Download the Spacy "brain"
RUN python -m spacy download en_core_web_sm

# 7. Open the port Streamlit uses
EXPOSE 8501

# 8. The command to launch your app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
