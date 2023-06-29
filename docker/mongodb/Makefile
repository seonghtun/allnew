build:
	docker build -t mongo .
run:
	docker run -it -d -p 27017:27017 --name mongo -v /Users/ysh97/Documents/GitHub/docker/mongo:/app -v /Users/ysh97/Documents/GitHub/docker/mongo/data:/data/db mongo
exec:
	docker exec -it mongo /bin/bash
logs:
	docker logs mongo 
ps:
	docker ps -a
img:
	docker images
rm:
	docker rm -f $$(docker ps -aq)
rmi:
	docker rmi $$(docker images -q)
