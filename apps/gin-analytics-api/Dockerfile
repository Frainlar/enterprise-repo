FROM golang:1.20 AS builder
WORKDIR /app
COPY go.mod .
RUN go mod download
COPY . .
RUN go build -o server .

FROM gcr.io/distroless/base
COPY --from=builder /app/server /server
EXPOSE 8080
CMD ["/server"]
