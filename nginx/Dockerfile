FROM tutum/nginx

RUN rm /etc/nginx/sites-enabled/default
RUN mkdir static
RUN mkdir /etc/dhparams
COPY dhparams  /etc/dhparams
COPY sites-enabled/ /etc/nginx/sites-enabled
