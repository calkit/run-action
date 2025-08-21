# Calkit run GitHub Action

A GitHub Action to run a Calkit project's pipeline and optionally save results
(commit and push) to Git and DVC.

## Usage

The example workflow below shows how to run a Calkit project, saving results.
Note the permissions, concurrency, and checkout options.
The action will also require a `dvc_token` input,
which should be set in the repository's Actions secrets.

```yaml
name: Run pipeline

on:
  push:
    branches:
      - main
  pull_request:

permissions:
  contents: write

# Make sure we only ever run one per branch so we don't have issues pushing
# after running the pipeline
concurrency:
  group: calkit-run-${{ github.ref }}
  cancel-in-progress: false

jobs:
  main:
    name: Run
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          # For PRs, checkout the head ref to avoid detached HEAD
          ref: ${{ github.head_ref || github.ref_name }}
          token: ${{ secrets.GITHUB_TOKEN }}
      - name: Configure Git credentials
        run: |
          git config user.name github-actions[bot]
          git config user.email 41898282+github-actions[bot]@users.noreply.github.com
      - name: Setup uv
        uses: astral-sh/setup-uv@v5
      - name: Install Calkit
        run: uv tool install calkit-python
      - name: Run Calkit
        uses: calkit/run-action@v1
        with:
          dvc_token: ${{ secrets.CALKIT_DVC_TOKEN }}
```

## Configuration

If simply running the pipeline is desired, the `save` option can be set to
`false`.
Additionally, caching DVC data can be disabled with `cache_dvc: false`.
