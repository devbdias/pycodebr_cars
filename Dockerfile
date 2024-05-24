# Use uma imagem base oficial do Python
FROM python:3.12-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie os arquivos de requisitos para o contêiner
COPY requirements.txt /app/

# Instale as dependências do Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copie o código da aplicação para o contêiner
COPY . /app/

# Crie o diretório de arquivos estáticos e defina permissões
RUN mkdir -p /app/staticfiles
RUN chmod -R 755 /app/staticfiles

# Defina as variáveis de ambiente do Django
ENV DJANGO_SETTINGS_MODULE=myproject.settings
ENV PYTHONUNBUFFERED=1

# Exponha a porta que o Django usará
EXPOSE 8000

# Comando para coletar arquivos estáticos
RUN python manage.py collectstatic --noinput || { echo 'collectstatic failed'; exit 1; }

# Comando para aplicar migrações
RUN python manage.py migrate

# Comando para iniciar o servidor Django
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]
