from glob import glob
from os.path import join
from database.config import conection_db


def run_migrations():
    with conection_db() as cursor:
        migrations = join("database", "migrations", "sql")
        for file in sorted(glob(f"{migrations}/*.sql")):
            print(f"Running migration {file}")
            with open(file, "r") as f:
                cursor.executescript(f.read())
