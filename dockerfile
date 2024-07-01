# Usa a imagem oficial do Python 3.8
FROM python:3.8

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos necessários para o contêiner
COPY ver.py /app/ver.py
COPY test_verificar.py /app/test_verificar.py

# Instala o pylint para análise de código (opcional)
RUN pip install pylint

# Comando para rodar os testes
CMD ["python", "-m", "unittest", "test_verificar.py"]
