FROM rust:1.72 AS builder
WORKDIR /app
COPY Cargo.toml .
COPY src ./src
RUN cargo build --release

FROM debian:buster-slim
COPY --from=builder /app/target/release/actix-core-api /usr/local/bin/app
EXPOSE 8080
CMD ["/usr/local/bin/app"]
