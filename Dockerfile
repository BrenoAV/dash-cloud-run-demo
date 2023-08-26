FROM python:3.11-slim

# Copy local code to the container image
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install depedencies
RUN pip install -r requeriments.txt

EXPOSE 8080

CMD ["python", "app.py"]