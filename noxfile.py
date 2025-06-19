import tempfile

import nox


@nox.session(reuse_venv=True)
def docs(session):
    session.install(".[docs]")
    session.run(
        "sphinx-build",
        "-b",
        "dirhtml",
        "-v",
        "docs/",
        "build/docs",
    )


@nox.session(name="serve", reuse_venv=True)
def serve(session):
    session.install("-e", ".[docs]")
    session.install("sphinx-autobuild")
    with tempfile.TemporaryDirectory() as destination:
        session.run(
            "sphinx-autobuild",
            "--port=0",
            "--watch=src/",
            "--ignore=src/sphinx_treeview/static/",
            "--open-browser",
            "-b=dirhtml",
            "-a",
            "docs/",
            destination,
        )
