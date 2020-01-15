# Kivu_exchanges


# Docker build

- Create a Digital ocean Droplet with docker by running : 

```
docker-machine create \
-d digitalocean \
--digitalocean-access-token Digital Ocean APi Cred\             
kivu-exchange
```

- Run `docker-machine build`

Once the build is successfull run 

- Run `docker-machine up -d`

Copy the static directory with the following command :

`docker cp app/static $(docker-compose ps -q nginx):/`
