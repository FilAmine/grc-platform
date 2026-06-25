# Architecture

The backend is organized around Clean Architecture boundaries.

## Dependency Rule

Dependencies point inward:

- `interfaces` depends on `application`.
- `application` depends on `domain`.
- `infrastructure` implements `domain` repository contracts.
- `domain` has no framework dependency.

## Request Flow

1. FastAPI route receives and validates a request.
2. Dependency providers wire concrete repositories into use case services.
3. Application services execute use cases against repository interfaces.
4. SQLAlchemy repositories persist and hydrate domain entities.
5. Routes serialize domain entities into API responses.

## Production Notes

- Configuration is environment-driven via Pydantic Settings.
- Structured JSON logging is configured with `structlog`.
- Alembic owns database schema migrations.
- Redis is available for caching, rate limiting, sessions, and background job coordination.
- Docker Compose provides local parity for PostgreSQL, Redis, backend, and frontend.
