from envparse import Env

env = Env()


DATABASE_URL = env.str(
    "DATABASE_URL",
    default="postgresql+asyncpg://postgres:@localhost:5432/med_data",
)
##DATABASE_URL = "postgresql+asyncpg://%{DB_USER}s:%{DB_PASS}s@%{DB_HOST}s:%{DB_PORT}s/%{DB_NAME}s",

