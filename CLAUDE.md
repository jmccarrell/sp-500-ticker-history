# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This project provides date-centric access to S&P 500 index membership over time. The primary API is `sp500_tickers_as_of(year, month, day)` which returns a frozenset of ticker symbols that were in the index on the specified date. Coverage spans from January 1, 2010 through at least August 18, 2026.

## Common Commands

This project uses `just` for task automation and `uv` for Python dependency management.

### Run python code
- use `uv run python` to execute python

### Testing
- Run all tests: `just test`
- Run specific test: `just test tests/test_sp500_2026.py`
- Run specific test function: `just test tests/test_sp500_2026.py::test_year_boundary_2025_2026`
- Run tests with coverage: `just cov` (generates HTML report in `htmlcov/`)

### Code Quality
- Run linters (ruff check + format): `just lint`
- Check types: `just typing`
- Run all checks: `just check-all` (lint + cov + typing)

### Dependency Management
- Install/sync dependencies: `just install` or `uv sync`
- Update dependencies: `just update` or `uv sync --upgrade`
- Clean and reinstall: `just fresh`

## Architecture

### Core Module: `src/sp_500_ticker_history/sp500tickers.py`

The main function `sp500_tickers_as_of(year, month, day)` works by:
1. Loading ticker data from YAML files via `_load_tickers_from_yaml(year)` (cached with `@lru_cache`)
2. Starting with the `tickers_on_Jan_1` set for the specified year
3. Applying any index changes (union/difference operations) that occurred on or before the query date
4. Returning the result as a frozenset

### Data Model: YAML Change Files

Each year has a YAML file (`sp500-ticker-changes-YYYY.yaml`) defining:
- `year`: integer year
- `tickers_on_Jan_1`: list of ticker symbols in the index on January 1st
- `changes`: optional map of ISO dates (YYYY-MM-DD) to change operations
  - `union`: tickers added to the index
  - `difference`: tickers removed from the index

Example:
```yaml
changes:
  '2025-05-19':
    difference:
      - DFS
    union:
      - COIN
```

YAML files use StrictYAML with a defined schema (`ticker_schema`) for validation.

### Test Structure

Tests are organized by year (`test_sp500_YYYY.py`). Each test file:
- Defines `num_tickers_YYYY` constant for the expected index size that year
- Tests year boundary continuity via `_test_at_year_boundary(year)` helper
- Tests individual ticker swaps via `_test_one_swap(date, removed, added, expected_count)` helper

Test helpers are defined in `tests/helpers.py`.

## Adding New Index Changes

When S&P announces index changes:
1. Update the appropriate YAML file in `src/sp_500_ticker_history/`
2. Add test cases in the corresponding `tests/test_sp500_YYYY.py` file
3. Tests should verify the swap occurred on the correct date
4. Update the coverage date in `CLAUDE.md` and `README.md`
5. Run `just check-all` before committing

## Releasing

Version follows CalVer format: `YYYY.minor.patch`

Tagging happens in CI, never locally. The version bump rides in on the ordinary
PR, and the Release workflow tags whatever `main` already says — so a tag can
never point at a commit that missed `main`.

### Cutting a release
1. Get the release version from the user
2. Update `pyproject.toml` with the new version
3. Open a PR with that change and merge it
4. Run `just release VERSION` (e.g. `just release 2026.11.0`)

`just release` only validates the CalVer format and dispatches the workflow
against `main`; it makes no commits and creates no tags. The equivalent by hand
is `gh workflow run release.yml --ref main -f version=VERSION`.

### The Release workflow
`.github/workflows/release.yml` runs on `workflow_dispatch` only — a pushed `v*`
tag no longer publishes anything. It:
1. Refuses to run unless dispatched against `main`
2. Validates the CalVer format
3. Verifies `pyproject.toml` already declares that version — merge the bump first
4. Verifies the tag does not already exist
5. Runs the test suite and builds with `uv build`
6. Creates and pushes the annotated `vVERSION` tag, only once the build is good
7. Creates a GitHub Release with auto-generated notes and build artifacts

It never commits, which is what keeps it clear of `main`'s branch protection —
`GITHUB_TOKEN` is not an admin and cannot push commits to `main`.

## Data Sources

The source of truth for S&P 500 ticker symbols is:
- Current components: https://en.wikipedia.org/wiki/List_of_S&P_500_companies#S&P_500_component_stocks
- Historical changes: https://en.wikipedia.org/wiki/Historical_components_of_the_S%26P_500

Wikipedia split the changes table out of `List_of_S&P_500_companies` on 2026-08-11; the old
anchor still resolves to the article, which no longer holds the table.

### Scraping Wikipedia

The two tables are on two pages, so scraping both means two requests. Use `httpx` + `BeautifulSoup` with `lxml` from the sibling project `../scrape-sp500-symbols/`. Run scraping scripts with that project's `uv run python`:

```python
import httpx
from bs4 import BeautifulSoup

CONSTITUENTS_URL = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
CHANGES_URL = "https://en.wikipedia.org/wiki/Historical_components_of_the_S%26P_500"
headers = {"User-Agent": "scrape-sp500-symbols/0.1 (https://github.com; educational project)"}


def fetch(url: str) -> BeautifulSoup:
    response = httpx.get(url, headers=headers, follow_redirects=True)
    response.raise_for_status()
    return BeautifulSoup(response.text, "lxml")


constituents_table = fetch(CONSTITUENTS_URL).find("table", {"id": "constituents"})
changes_table = fetch(CHANGES_URL).find("table", {"id": "changes"})
```

The changes table records constituent swaps only. A company that stays in the index under a new
ticker never appears there, so the constituents table is what catches a rename.

## Notes

- Python 3.14+ required
- Line length: 108 characters (configured in `ruff.toml`)
- Import sorting enabled via ruff (isort rules)
- Coverage settings: branch coverage enabled, shows missing lines, skips covered lines
