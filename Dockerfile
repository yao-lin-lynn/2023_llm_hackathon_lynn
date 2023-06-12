FROM python:3.9.10-buster
ENV TZ=Asia/Tokyo

RUN mkdir /work

WORKDIR /work
COPY ./ /work
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3333

CMD ["jupyter-lab", "--port=3333", "--no-browser", "--ip=0.0.0.0", "--allow-root"]



