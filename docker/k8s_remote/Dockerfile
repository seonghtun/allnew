# Step 1:
FROM node:16.20

# Step 2:
WORKDIR /usr/src/app

# Step 3:
COPY remoteapi.tar.gz .
RUN tar xvzf remoteapi.tar.gz
WORKDIR /usr/src/app/remoteapi
RUN npm install

# Step 4:
EXPOSE 8000

# Step 5:
CMD ["node", "app.js"]
