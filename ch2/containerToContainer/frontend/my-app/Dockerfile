# Use an official Node.js runtime as a base image
FROM node:14

# Set the working directory to /app
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install app dependencies
RUN npm install

# Copy the content of the local src directory to the working directory
COPY . .

# Build the React app
RUN npm run build

# Define the command to run the app
CMD ["npm", "start"]
