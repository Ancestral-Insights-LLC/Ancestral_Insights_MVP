FROM node:14  # Use the official Node.js 14 image as a parent image
WORKDIR /usr/src/app  # Set the working directory in the container to /usr/src/app
COPY package*.json ./  # Copy package.json and package-lock.json to the working directory in the container
RUN npm install  # Install dependencies
COPY . .  # Copy the rest of the files to the working directory in the container
EXPOSE 8080  # Make port 8080 available to the world outside this container
CMD [ "node", "server.js" ]  # Run server.js when the container launches
