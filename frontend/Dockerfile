FROM node:16.10-bullseye
RUN \
    apt-get --allow-releaseinfo-change update && \
    apt-get install git -y && \
    git config --global user.email "angular@email.com" && \
    git config --global user.name "Angular User"
WORKDIR /main/angularExample
COPY ./frontend/angularExample/package.json ./
COPY ./frontend/angularExample/tsconfig.app.json ./
COPY ./frontend/angularExample/src/styles.scss ./src/styles.scss
RUN npm install
RUN npm install --save @angular/material @angular/cdk
CMD ["npm", "start"]