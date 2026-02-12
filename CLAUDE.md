# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This project provides date-centric access to S&P 500 index membership over time. The primary API is `sp500_tickers_as_of(year, month, day)` which returns a frozenset of ticker symbols that were in the index on the specified date. Coverage spans from January 1, 2020 through at least February 9, 2026.

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

### Cutting a release
1. Get the release version from the user
2. Ensure all changes are merged to `main` — run `just release` only from `main`
3. Run `just release VERSION` (e.g. `just release 2026.2.0`)

The `just release` recipe:
- Validates the version format
- Checks for uncommitted changes
- Updates the version in `pyproject.toml`, commits, and creates an annotated `vVERSION` tag
- Pushes the commit and tag to origin

### Automated GitHub Release
Pushing a `v*` tag triggers the `.github/workflows/release.yml` workflow, which:
1. Verifies the tag version matches `pyproject.toml`
2. Runs the test suite
3. Builds the distribution with `uv build`
4. Creates a GitHub Release with auto-generated notes and build artifacts

## Data Sources

The source of truth for S&P 500 ticker symbols is:
- Current components: https://en.wikipedia.org/wiki/List_of_S&P_500_companies#S&P_500_component_stocks
- Historical changes: https://en.wikipedia.org/wiki/List_of_S&P_500_companies#Selected_changes_to_the_list_of_S&P_500_components

## Notes

- Python 3.14+ required
- Line length: 108 characters (configured in `ruff.toml`)
- Import sorting enabled via ruff (isort rules)
- Coverage settings: branch coverage enabled, shows missing lines, skips covered lines
