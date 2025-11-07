# Calkit run GitHub Action

A GitHub Action to run a Calkit project's pipeline and optionally save results
(commit and push) to Git and DVC.

## Usage

The example workflow below shows how to run a Calkit project, saving results.
Note the permissions, concurrency, and checkout options.
The action will also require a `dvc_token` input,
which should be set in the repository's Actions secrets.

<!-- snippet:example.yml:start -->
```yaml
# Auto-generated from example.yml — do not edit this block by hand.
```
<!-- snippet:example.yml:end -->

## Configuration

If simply running the pipeline is desired, the `save` option can be set to
`false`.
Additionally, caching DVC data can be disabled with `cache_dvc: false`.
