build:
	docker build -t mongo .
run:
<<<<<<< HEAD
	docker run -it -d -p 27017:27017 --name mongo -v /Users/ysh97/Documents/GitHub/docker/mongo:/app -v /Users/ysh97/Documents/GitHub/docker/mongo/data:/data/db mongo
exec:
	docker exec -it mongo /bin/bash
logs:
	docker logs mongo 
=======
	docker run -d -p 27017:27017 -v /Users/MINHUI/Documents/GitHub/docker/mongo:/app -v /Users/MINHUI/Documents/GitHub/docer/mongo/data:/data/db --name mongo mongo
exec:
	docker exec -it mongo /bin/bash
logs:
	docker logs mongo
>>>>>>> 09bf0f88c66266c141ffbbc20a12f146f09927bb
ps:
	docker ps -a
img:
	docker images
rm:
	docker rm -f $$(docker ps -aq)
rmi:
	docker rmi $$(docker images -q)
