# Step 1:
FROM node:16.20

# Step 2:
WORKDIR /usr/src/app

# Step 3:
COPY weather.tar.gz .
RUN tar xvzf weather.tar.gz
WORKDIR /usr/src/app/weather
RUN npm install
RUN npm install -g nodemon

# Step 4:
EXPOSE 8000

# Step 5:
CMD ["nodemon", "app.js"]
