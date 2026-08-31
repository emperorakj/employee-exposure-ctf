FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
COPY templates ./templates
ENV FLAG="EH4X{1D0R_l34k5_m0r3_th4n_y0u_th1nk}"
EXPOSE 5000
CMD ["python", "app.py"]
