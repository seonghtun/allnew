<<<<<<< HEAD
# Step 1:
FROM node:16

# Step 2
WORKDIR /usr/src/app

# Step 3
RUN git clone http://github.com/seonghtun/docker-publish
WORKDIR docker-publish/worldcup
RUN npm install

# Step 4
EXPOSE 8000

# Step 6
=======
# step 1
FROM node:16

# step 2
WORKDIR /usr/src/app

# step 3
RUN git clone http://github.com/westmini427/docker-publish
WORKDIR docker-publish/worldcup
RUN npm install

# step 4
EXPOSE 8000

# step 6
>>>>>>> 09bf0f88c66266c141ffbbc20a12f146f09927bb
CMD ["node", "app.js"]
