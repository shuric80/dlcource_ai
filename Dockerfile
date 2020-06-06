FROM  continuumio/miniconda3

RUN apt-get update && \
        conda install jupyter -y --quiet && \
        conda install pandas && \
        conda install numpy && \
        conda install matplotlib && \
        conda install scipy && \
        apt-get clean && \
        rm -rf /var/lib/apt/lists/*


USER root

EXPOSE 8888

WORKDIR /opt/project
COPY jupyter_notebook_config.json  /root/.jupyter/jupyter_notebook_config.json
VOLUME ["/opt/project"]

CMD ["/opt/conda/bin/jupyter", "notebook", "--notebook-dir=/opt/project", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
