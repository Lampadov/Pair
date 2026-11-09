"""Read-only audit of merged PRs containing coauthor trailers; requires gh."""
import argparse
import json
import re
import subprocess


def api_pages(endpoint):
    result = subprocess.run(
        ["gh", "api", "--paginate", endpoint],
        check=True, capture_output=True, text=True,
    )
    remaining = result.stdout.lstrip()
    items = []
    decoder = json.JSONDecoder()
    while remaining:
        page, end = decoder.raw_decode(remaining)
        items.extend(page)
        remaining = remaining[end:].lstrip()
    return items


def coauthors(message):
    return re.findall(r"^Co-authored-by:\s*(.+?)\s*<([^<>\s]+)>\s*$", message, re.MULTILINE | re.IGNORECASE)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repository", help="owner/repository")
    parser.add_argument("--limit", type=int, help="Inspect only the latest N merged PRs")
    args = parser.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", args.repository):
        parser.error("repository must be owner/repository")
    if args.limit is not None and args.limit < 1:
        parser.error("--limit must be positive")
    pulls = api_pages(f"repos/{args.repository}/pulls?state=closed&per_page=100&sort=updated&direction=desc")
    merged = [pr for pr in pulls if pr["merged_at"]]
    inspected = merged[:args.limit] if args.limit else merged
    matches = []
    for pr in inspected:
        commits = api_pages(f"repos/{args.repository}/pulls/{pr['number']}/commits?per_page=100")
        if any(coauthors(c["commit"]["message"]) for c in commits):
            matches.append(pr["number"])
    print(json.dumps({"repository": args.repository, "merged_prs": len(merged),
                      "inspected_prs": len(inspected), "prs_with_coauthor_trailers": matches,
                      "note": "Candidate PRs only; GitHub determines achievement eligibility."}, indent=2))


if __name__ == "__main__":
    main()
