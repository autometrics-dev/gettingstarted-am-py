# Sample Python FastAPI app with Autometrics

This is a sample backend service written in Python with the FastAPI framework with several API handlers that are erroring or responding slowly intended to showcase the Autometrics framework with Service Level Objectives.

### Resources

- see the [documentation site](https://docs.autometrics.dev) for more in-depth information on all Autometrics features.
- ask for help and share feedback on [our Discord](https://discord.com/invite/MJr7pYzZQ4)!

## Getting started

To get the sample up and running you can follow these steps:

1. Clone the repository and install the dependencies

```bash
git clone autometrics-dev/gettingstarted-am-py

cd gettingstarted-am-py

pip install -r requirements.txt
```

2. Download the Autometrics CLI

If you're on macOS you can use Homebrew:

```bash
brew install autometrics-dev/tap/am
```

or you can grab the binaries directly from the [GitHub release](https://github.com/autometrics-dev/am/releases/).

3. Start the application

```bash
python uvicorn main:app --reload
```

The application will start on a port 8080 by default and expose a metrics endpoint.

4. Start the Autometrics CLI and Explorer

Start the Autometrics CLI and point it to the endpoint it can scrape metrics from.

```bash
am start :8080
```

Autometrics CLI will download and run a Prometheus binary under the hood and start scraping metrics.

5. Preview the metrics in Autometrics Explorer

Autometrics CLI will also start a server with the Explorer available on `localhost:6789`. You can browse it and start exploring your sample app metrics! (You might need to ping the endpoints a few times to see the data reflected).

That's all!


