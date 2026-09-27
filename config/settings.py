# single source file for all the configuration
# without centralized settings, devs os.getenv() across 30 files
# Ex - if env var name changes

# Pydantic settings
# all env vars are defined in one place - settings.py

from email.policy import default
from mosiac.ingestion import clinical_trials_client
from pydantic_settings import BaseSettings, SettingsConfigDict
# BaseSettings : it knows how to read values from env variables & .env files
# SettingsConfigDict : how we config base settings behaviour

from pydantic import Field
# Filed : adds metadata to each settings

class Settings(BaseSettings):
    '''
    all config defined in one place only
    case insensitive : open_api_key =OPENAI_API_KEY
    '''
    model_config = SettingsConfigDict(
        env_file = ".env",
        env_file_encoding = "utf-8",
        case_sensitive = False,
        extra = "ignore",
    )

    openai_api_key : str = Field(
        ...,
        description = "Open AI API KEY for LLM & Embeddings"
    )

    openai_embedding_model : str = Field(
        default = "text-embedding-3-large",
        description = "OpenAI model used to generate the vector embeddings"
    )

    openai_chat_model : str = Field(
        default = "gpt-4o",
        description = "OpenAI model used for agent reasoning"
    )

    langsmith_project : str = Field(
        default = "clinical_trail_intillegence",
        description = "Langsmith project name"
    )

    langsmith_tracing_v2 : bool = Field(
        default = True,
        description = "Enable langsmith tracing for all the agentic runs"
    )

    gcp_project_id : str = Field(
        ...,
        description = "GCP project ID"
    )

    gcp_region : str = Field(
        default = "us-central",
        description = "GCP region for all cloud resources"
    )

    gcp_bucket_name : str = Field(
        ...,
        description = "Google cloud storage bucket name"
    )

    db_host : str = Field(
        ...,
        description = "Cloud SQL host IP (LOCAL) or socket path (Cloud run)"
    )

    db_port : str = Field(
        default = 5432,
        description = "PostgresSQL port"
    )
    
    db_name : str = Field(
        default = "clinical_trial_db",
        description = "postgres sql db name"
    )

    db_user : str =  Field(
        ...,
        description = "postgreSQL DB user"
    )

    db_password : str = Field(
        ...,
        description = "PostgeSQL dayabase password"
    )

    clinical_trials_base_url : str =Field(
        default = "https://clinicaltrials.gov/api/v2",
        description = "ClinicalTrails.govAPI v2 base URL"
    )

    clinical_trail_page_size :  str = Field(
        default = 100,
        description = "number of studies to fetch per API page"
    )

    pubmed_base_url : str = Field(
        default = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils",
        description="pubmed eutils API based URL"
    )

    api_host : str = Field(
        default = "0.0.0.0",
        description = "Fast API host address"
    )

    api_port : str = Field(
        default = 8000,
        description = "Fast API port"
    )

    api_env : str = Field(
        default = "development",
        description = "Environment name development or production"
    )

    @property
    def database_base_url(self) -> str:
        '''
        builds the full async postgreSQL connection string from parts
        we use asyncpg as the async postgreSQL driver
        asyncpg requires the connection string to start with :
        postgreSQL+asyncpg://

        returns :
        str : full connection url ready for asyncpg.create_pool()
        example : postgreSQL+asyncpg://mosiac_user:password@IP_address:port_no/mosaic
        '''

        return (
            f"postgresql+asyncpg://{self.db_user}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )
    
    @property
    def is_production(self) -> bool:
        '''
        returns True if the app is running in production

        '''
        return self.api_env.lower() == "production"
    
# singleton instance
settings = Settings()

# from mosiac.config.settings import settings
    
 
    