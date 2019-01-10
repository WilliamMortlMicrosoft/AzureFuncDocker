FROM mcr.microsoft.com/azure-functions/python:2.0

ENV AzureFunctionsJobHost__Logging__Console__IsEnabled=true

COPY src /home/site/wwwroot

RUN cd /home/site/wwwroot && \
    pip install -r requirements.txt