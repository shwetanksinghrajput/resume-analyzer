FROM python:3.11-slim

WORKDIR /app

# Install absolute essentials and clean up
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and setuptools to handle complex dependencies
RUN pip install --upgrade pip setuptools wheel

COPY . .

# Install simplified requirements
RUN pip install --no-cache-dir -r requirements.txt

# Download the spaCy model
RUN python -m spacy download en_core_web_sm

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.enableCORS=false", "--server.enableXsrfProtection=false"]
