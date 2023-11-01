from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def get_database_url(self):
        user = f'{self.DB_USER}:{self.DB_PASS}'
        database = f'{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
        return f"postgresql+asyncpg://{user}@{database}"
    
    # Для создания токена
    SECRET_KEY: str
    ALGORITHM: str


    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
print(settings.get_database_url)