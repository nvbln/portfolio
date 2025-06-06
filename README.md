# Portfolio template

A template I made for portfolio websites using [Pelican](https://getpelican.com/). Consists of an home (index) page similar to a CV, and a project page, that one can fill with details on the project.

### Install

There are two possible installation methods:
1. Install a container application like [Docker](https://docs.docker.com/engine/install/) or [Podman](https://podman.io/docs/installation).
2. Install the [Pelican](https://getpelican.com/#quickstart) application natively. For this you will need to install either [pipx](https://pipx.pypa.io/stable/installation/) (recommended) or [pip](https://pip.pypa.io/en/stable/installation/). In the case of `pipx`, make sure to replace `pip` with `pipx` in the Pelican installation guide.

### Run

#### Docker

The application can be run through Docker using the following command:

```docker compose up```

The website is then be available at `localhost:80`. The website will be automatically updated as the content gets updated.

#### Pelican

If Pelican is installed natively, run it with the following command from the repository directory to access it from your browser with automatic reloading upon changes:

```pelican --bind 127.0.0.1 --listen --autoreload -t .```
