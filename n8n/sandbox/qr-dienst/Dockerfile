# AI-assisted: Claude (Fable 5.1), human-reviewed: ausstehend, Stand 12.09.2026
# QR-Dienst für die n8n-Sandbox: Python-Standardbibliothek plus qrcode und Pillow, läuft ohne Root.
FROM python:3.12-alpine
RUN pip install --no-cache-dir qrcode==8.2 pillow==11.3.0 && adduser -D -H qr
COPY qr_dienst.py /app/qr_dienst.py
USER qr
EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=3s CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/health', timeout=2)" || exit 1
CMD ["python", "/app/qr_dienst.py"]
