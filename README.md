# kustomization at tubi

![](docs/diagrams/outputs/mermaid-diagram.svg)

## Guiding Principles

* Follow [this guide](https://kubectl.docs.kubernetes.io/guides/app_deployment/accessing_multiple_clusters/)
* Use [official terminology](https://kubectl.docs.kubernetes.io/references/kustomize/glossary/)

## Getting Started

* See [Quickstart](docs/quickstart.md) for initial first steps
* See [Learning](docs/learning.md) for learning kustomize
* See [Repo layout](docs/repo-layout.md) for conventions that are used by Tubi
* See [Style guide](docs/style-guide.md) for style guide

## Common Workflows

### Application Developers

* [Creating new apps](docs/workflows/apps/new-app.md)
* [Customizing apps](docs/workflows/apps/customize.md)
* [Deploying apps](docs/workflows/apps/deploy.md)

### Infrastructure Developers

* [Creating new environments](docs/workflows/infra/new-environment.md)
* [Creating cluster resources](docs/workflows/infra/cluster-resources.md)
* [Creating reusable sidecar patches](docs/workflows/infra/sidecars.md)
