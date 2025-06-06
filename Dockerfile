FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    nginx \
    python3 \
    pipx

# Remove the apt cache
RUN rm -rf /var/lib/apt/lists/*

RUN python3 -m pipx install "pelican[markdown]"

WORKDIR /app

EXPOSE 8000

ENTRYPOINT ["sh", "-c", "exec /root/.local/bin/pelican --bind 0.0.0.0 --listen"]
