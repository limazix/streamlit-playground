# Streamlit Playground [![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](http://commitizen.github.io/cz-cli/)

### Requirements

- [Python](https://python.org) **(v3.11+)**
- [PDM](https://pdm-project.org) **(v2.22+)**

## Usage
### Install Dependencies

```sh
pdm install
```

### <a id="commits"/> Commits

This project uses the [Semantic Version](http://semver.org) pattern to generate the package release and it changelogs. To make it work properly, it implement a different flow of actions for commits.


```sh
pdm run commit # start the commit pipeline
```

The commit pipeline is supported by the [Commitizen](https://commitizen-tools.github.io/commitizen/) module. The first one is a cli tool that guide the devloper through the commit pipeline by inquiring for what need to be done. And the second one check if the generated commit follows the [Semantic Version](http://semver.org) pattern.