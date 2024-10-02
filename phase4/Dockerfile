# Switch to Debian Buster Slim
FROM debian:buster-slim AS builder

# Set shell options for better error handling
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Update and install required packages without specific version numbers
RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    libffi-dev \
    libgmp-dev \
    zlib1g-dev \
    curl \
    ca-certificates \
    git \
    netbase \
 && curl -sSL https://get.haskellstack.org/ | sh \
 && rm -rf /var/lib/apt/lists/*


# Install dependencies and build the application
COPY . /opt/hadolint
RUN scripts/fetch_version.sh \
  && stack install --ghc-options="-fPIC" --flag hadolint:static

# Compress with UPX
RUN curl -sSL https://github.com/upx/upx/releases/download/v3.94/upx-3.94-amd64_linux.tar.xz \
  | tar -x --xz --strip-components 1 upx-3.94-amd64_linux/upx \
  && ./upx --best --ultra-brute /root/.local/bin/hadolint

# Create a smaller runtime image based on Debian
FROM debian:buster-slim AS debian-distro
COPY --from=builder /root/.local/bin/hadolint /bin/
CMD ["/bin/hadolint", "-"]

# Use a minimal scratch image for the final stage
FROM scratch AS distro
COPY --from=builder /root/.local/bin/hadolint /bin/
CMD ["/bin/hadolint", "-"]

# Alpine-based image for a smaller footprint
FROM alpine:3 AS alpine-distro
COPY --from=builder /root/.local/bin/hadolint /bin/
CMD ["/bin/hadolint", "-"]
