# AI-assisted: Claude, human-reviewed ausstehend, Stand 16.09.2026
FROM python:3.12-alpine
RUN adduser -D -H tuer
COPY tuersteher.py /app/tuersteher.py
USER tuer
EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=3s CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/health', timeout=2)" || exit 1
CMD ["python", "/app/tuersteher.py"]
