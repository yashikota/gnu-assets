FROM alpine:3.21

# Alpine uses musl libc by default — all binaries built here are fully static
RUN apk add --no-cache \
        build-base \
        curl \
        gnupg \
        python3 \
        py3-yaml \
        texinfo \
        ca-certificates \
        bash \
        coreutils \
        findutils \
        gzip \
        xz \
        tar

WORKDIR /workspace
