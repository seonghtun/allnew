build:
	docker build -t nodejs .
run:
	docker run -it --name nodejs -d -p 8000:8000 nodejs
exec:
	docker exec -it ubuntu /bin/bash
start:
	docker start nodejs
stop:
	docker stop nodejs
logs:
	docker logs nodejs
ps:
	docker ps -a
img:
	docker images
rm:
	docker rm -f $$(docker ps -aq)
rmi:
	docker rmi $$(docker images -q)
