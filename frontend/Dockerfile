FROM node:20-alpine

WORKDIR /app

# Copy package files
COPY package.json package-lock.json* ./

# Install dependencies
RUN npm install

# Expose port and run dev server
EXPOSE 3000
CMD ["npm", "run", "dev"]
