FROM node:20

WORKDIR /flask-app

# Copy package files first
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application
COPY . .

# Set the default command
CMD ["npm", "run", "dev"]