build:
	docker build -t nodejs .
run:
<<<<<<< HEAD
	docker run -it -d -p 8000:8000 --name nodejs -v /Users/ysh97/Documents/GitHub/nodejs:/app nodejs 
=======
	docker run -it -d -p 8000:8000 -v /User/MINHUI/Document/GitHub/nodejs:/app --name nodejs nodejs
>>>>>>> 09bf0f88c66266c141ffbbc20a12f146f09927bb
exec:
	docker exec -it nodejs /bin/bash
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
