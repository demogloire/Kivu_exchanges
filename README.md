# Kivu_exchanges


# Docker build

- Create a Digital ocean Droplet with docker by running : 

```
docker-machine create \
-d digitalocean \
--digitalocean-access-token 5eee9b9f5373c21bfd53c2a9a5e567a27f4d8e579ed5c5b42801bb09608d7947\             
kivu-exchange
```

docker-machine create \
-d digitalocean \
--digitalocean-access-token ADD_YOUR_TOKEN_HERE \
production

- Run `docker-machine build`

Once the build is successfull run 

- Run `docker-machine up -d`

Copy the static directory with the following command :

`docker cp app/static $(docker-compose ps -q nginx):/`
