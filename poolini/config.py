from dotenv import load_dotenv
from envyaml import EnvYAML


CONFIG_FILE = "poolini/config.yml"

load_dotenv()
config = EnvYAML(CONFIG_FILE, strict=False)
