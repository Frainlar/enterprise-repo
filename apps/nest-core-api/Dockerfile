FROM oven/bun:1.0 as base
WORKDIR /app
COPY package.json .
RUN bun install
COPY . .
CMD ["bun", "run", "src/main.ts"]
