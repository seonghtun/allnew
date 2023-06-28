# Step 1:
FROM node:16.20

# Step 2 : Package Install
RUN apt -y update && apt -y upgrade && apt -y install git net-tools vim

# Step 3 : Specify a working directory
WORKDIR '/root'

# Step 4 : Config file copy
COPY .bashrc .
COPY .exrc .
COPY hello.js .

# Step 5 : install express
RUN npm init -y 
RUN npm install express
RUN npm install -g nodemon

# Step 6 : open port
EXPOSE 8000

# Step 7 : Execution Program
CMD ["nodemon", "hello.js"]

