# Pair

Read-only tools for inspecting pair-programming pull requests.

## Audit merged pull requests

Requires Python 3 and an authenticated GitHub CLI (`gh`).

```sh
python pair_progress.py Lampadov/pair-sessions --limit 3
python -m unittest -v
```

Omit `--limit` to inspect every merged PR. Results identify commits with
`Co-authored-by` trailers, not GitHub's internal achievement counter.
The tool does not create commits, modify repositories, or award achievements.
GitHub controls badge eligibility and updates.
