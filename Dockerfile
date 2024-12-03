# Node.js의 공식 이미지를 기반으로 사용
FROM node:14

# 작업 디렉터리를 설정
WORKDIR /app

# package.json과 package-lock.json 복사
COPY package*.json ./

# 의존성 설치
RUN npm install

# 애플리케이션 소스 코드 복사
COPY . .

# 컨테이너가 실행될 때 실행할 명령어
CMD ["node", "app.js"]

# 애플리케이션에서 사용하는 포트 노출
EXPOSE 3000
