build:
	docker build -t mysql .
run:
<<<<<<< HEAD
	docker run -it -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=1234 --name mysql -v /Users/ysh97/Documents/GitHub/mysql:/app mysql 
exec:
	docker exec -it mysql /bin/bash
logs:
	docker logs mysql 
=======
	docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=1234 -v /Users/MINHUI/Documents/GitHub/mysql:/app --name mysql mysql
exec:
	docker exec -it mysql /bin/bash
logs:
	docker logs mysql
>>>>>>> 09bf0f88c66266c141ffbbc20a12f146f09927bb
ps:
	docker ps -a
img:
	docker images
rm:
	docker rm -f $$(docker ps -aq)
rmi:
	docker rmi $$(docker images -q)
