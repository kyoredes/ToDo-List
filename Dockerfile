FROM python

WORKDIR /

RUN pip install uv

COPY . .

RUN uv sync

EXPOSE 8000

ENV PATH="/app/.venv/bin:$PATH"

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
CMD ["uv", "run", "fastapi", "dev", "--port", "8000"]
