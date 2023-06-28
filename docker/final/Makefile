build:
	docker build -t nodejs .
run:
<<<<<<< HEAD
	docker run -it --name nodejs -d -p 8000:8000 nodejs
=======
	docker run -d -p 8000:8000 --name nodejs nodejs
>>>>>>> 09bf0f88c66266c141ffbbc20a12f146f09927bb
exec:
	docker exec -it nodejs /bin/bash
start:
	docker start nodejs
<<<<<<< HEAD
attach:
	docker attach nodejs
=======
stop:
	docker stop nodejs
>>>>>>> 09bf0f88c66266c141ffbbc20a12f146f09927bb
logs:
	docker logs nodejs
ps:
	docker ps -a
img:
	docker images
rm:
	docker rm -f $$(docker ps -aq)
rmi:
<<<<<<< HEAD
	docker rmi $$(docker images -q)
=======
	docker rmi $$(docker images -q)
>>>>>>> 09bf0f88c66266c141ffbbc20a12f146f09927bb
