FROM alpine/git:1.0.7

COPY LICENSE README.md entrypoint.sh recreate_conda_reqs.py /

RUN apk add python3
RUN pip3 install pipreqs
RUN pip3 install yaml

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
