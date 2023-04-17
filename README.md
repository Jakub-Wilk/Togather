# Setting up the dev environment

1. Install WSL2
2. Install docker

   2a. If you want to work on the API, you need to install the dependencies in your local environment to get syntax highlighting. You can either do it through Poetry (recommended), or through `pip install .` while in the `src/backend/` directory.
3. Run `docker compose up <service>`, where `<service>` is the service that you want to work on - `frontend`, `api`, or leave it empty if you want to work on both
4. Wait for the image(s) to build (only this first build takes this long), then exit with Ctrl+C
5. If you're working on the API, run `docker compose up migrate`, then `docker compose run api python3 manage.py createsuperuser` and go through the steps of creating an admin user

# Working with the dev environment

### Project-wide config

To configure some basic settings, you can create a `.env` file in the project root, however it is not mandatory.

Available variables to set:

- `VUE_PORT` - The port to which the frontend app will bind to, defaults to `5000` if not set
- `DJANGO_PORT` - The port to which the API will bind to, defaults to `8000` if not set
- More will be available in the future, when we migrate to PostgreSQL

### Frontend development

If you're working on frontend-specific features, to start the dev server you can just run `docker compose up frontend`, otherwise if you need the API up too, run `docker compose up`. If you want the container(s) to run in the background, add the `-d` flag after `up`. The app will be available on `http://localhost:${VUE_PORT}`.

### API development

To run the API, run `docker compose up api`. If you want the container to run in the background, add the `-d` flag after `up`. The API will be available on `http://localhost:${DJANGO_PORT}`. Warning: The dev server will display `0.0.0.0` as the host, but that's because it's running in a container and needs to be exposed to your local machine. Use `localhost` to connect to it.

If you need to migrate the database, run `docker compose up migrate`. That both makes the migrations, and migrates the database.

To add new modules to the project, you can either use Poetry (recommended), or manually add them to `pyproject.toml` under `[tool.poetry.dependencies]`
