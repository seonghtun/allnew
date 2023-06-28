<<<<<<< HEAD
# Step 1:
FROM node:16.20

# Step 2 : Package Install
RUN apt -y update && apt -y upgrade && apt -y install git net-tools vim

# Step 3 : Specify a working directory
WORKDIR '/root'

# Step 4 : Config file copy
=======
# step 1 : Base Images
FROM node:16.20.0

# step 2 : Package Install
RUN apt -y update && apt -y upgrade && apt -y install git net-tools vim

# step 3 : Specify a working directory
WORKDIR '/root'

# step 4 : Config file copy
>>>>>>> 09bf0f88c66266c141ffbbc20a12f146f09927bb
COPY .bashrc .
COPY .exrc .
COPY hello.js .

<<<<<<< HEAD
# Step 5 : install express
RUN npm init -y 
=======
# step 5 : install express
RUN npm init -y
>>>>>>> 09bf0f88c66266c141ffbbc20a12f146f09927bb
RUN npm install express
RUN npm install -g nodemon

# Step 6 : open port
EXPOSE 8000

# Step 7 : Execution Program
<<<<<<< HEAD
CMD ["nodemon", "hello.js"]

=======
CMD ["nodemon", "hello.js"]
>>>>>>> 09bf0f88c66266c141ffbbc20a12f146f09927bb
