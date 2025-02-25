from setuptools import setup

setup(
    name="spotifyCLI",
    version="0.1.0",
    py_modules=["spotifyCLI"],
    install_requires=["click", "spotipy", "dotenv"],
    entry_points={
        "console_scripts": [
            "spotifycli = spotifyCLI:cli" 
        ],
    },
)
