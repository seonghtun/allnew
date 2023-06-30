build:
	docker build -t weather .
run:
	docker run -it --name weather -d -p 8000:8000 weather
exec:
	docker exec -it weather /bin/bash
start:
	docker start weather
stop:
	docker stop weather
logs:
	docker logs weather
ps:
	docker ps -a
img:
	docker images
rm:
	docker rm -f $$(docker ps -aq)
rmi:
	docker rmi $$(docker images -q)
k8sinit:
	docker commit weather weathers
	docker tage weathers dockermana79/weather
	docker push dockermana79/weather
	docker rm -f $$(docker ps -aq)
	docker rmi dockermana79/weather
	docker rmi $$(docker images -q)
appdep:
	kubectl apply -f deployment.yaml
appsvc:
	kubectl apply -f service.yaml
getdep:
	kubectl get deployment
getsvc:
	kubectl get svc -o wide
getpod:
	kubectl get pod -o wide
delsvc:
	kubectl deletet svc weather
deldep:
	kubectl deletet deployment weather
