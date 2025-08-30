FROM node:20-alpine AS build

# Enable corepack for pnpm
RUN corepack enable

WORKDIR /app

# Copy package files
COPY apps/web/package.json apps/web/pnpm-lock.yaml* ./

# Install dependencies
RUN pnpm install --frozen-lockfile

# Copy source code
COPY apps/web ./

# Build the application
RUN pnpm build

# Production stage
FROM node:20-alpine AS production

RUN corepack enable

WORKDIR /app

# Copy built application from build stage
COPY --from=build /app/.next ./.next
COPY --from=build /app/package.json ./package.json
COPY --from=build /app/pnpm-lock.yaml* ./
COPY --from=build /app/node_modules ./node_modules
COPY --from=build /app/public ./public

ENV NODE_ENV=production
ENV PORT=3000

EXPOSE 3000

CMD ["pnpm", "start"]
