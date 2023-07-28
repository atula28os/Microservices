FROM okteto/python-fastapi

ENV PYTHONUNBUFFERED=True

RUN mkdir -p /app

COPY . main.py /app/

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8080

CMD [ "main.py" ]

ENTRYPOINT [ "python" ]

