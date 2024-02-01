# Mono Glenans ⛵

[![pipeline status](https://gitlab.com/dashboard-streamlit/mono-glenans/badges/main/pipeline.svg)](https://gitlab.com/dashboard-streamlit/mono-glenans/-/commits/main)
[![coverage report](https://gitlab.com/dashboard-streamlit/mono-glenans/badges/main/coverage.svg)](https://gitlab.com/dashboard-streamlit/mono-glenans/-/commits/main)
[![Latest Release](https://gitlab.com/dashboard-streamlit/mono-glenans/-/badges/release.svg)](https://gitlab.com/dashboard-streamlit/mono-glenans/-/releases)

* Deployment link on [https://mono-glenans.streamlit.app/](https://mono-glenans.streamlit.app/)
* Main repo on [Gitlab 🦊](https://gitlab.com/dashboard-streamlit/mono-glenans) and push mirror of [Github](https://github.com/Tonow/mono-glenans)
  * Please do the Merge request on **Gitlab 🦊** 🙏

## Code quality

this project use :
* [pre-commit](https://pre-commit.com/)
  * [ruff](https://docs.astral.sh/ruff/integrations/#pre-commit)

## Parts infos

* [stage](stage/README.md)

## Run or use locally

- [ ] set virtual environment
- [ ] install requirement
    ```shell
    pip install -r requirements.txt
    ```
- [ ] run
    ```shell
    streamlit run dashboard.py
    ```

## Run tests

- [ ] set virtual environment
- [ ] run tests
    ```shell
    pip install -r requirements-dev.txt
    ```
- [ ] run tests
    ```shell
    python -m pytest  --cov --cov-report term
    ```
