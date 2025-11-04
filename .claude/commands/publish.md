---
description: Publish CLI package to PyPI with version bumping (project)
---

# Publish Package

You are tasked with preparing a release via Pull Request.

## New Workflow (with branch protection):

Since main is protected, you must create a PR with version changes:

1. **Check current branch:**
   - Ensure you're not on main: `git branch --show-current`
   - If on main, create a new branch: `git checkout -b release/vX.Y.Z`

2. **Determine version bump:**
   - Default to patch version bump unless user specifies major or minor
   - Read current version from `pyproject.toml`
   - Calculate new version (e.g., 0.1.2 → 0.1.3 for patch)

3. **Update version:**
   - Modify the version in `pyproject.toml`
   - Update `uv.lock` by running `uv lock`

4. **Commit changes:**
   - Run `git status` and `git diff` to verify changes
   - Stage `pyproject.toml` and `uv.lock`
   - Commit with message: "Bump version to X.Y.Z"
   - Push branch: `git push -u origin release/vX.Y.Z`

5. **Create Pull Request:**
   - Use `gh pr create` to create a PR to main
   - Title: "Release vX.Y.Z"
   - Body should include:
     - Version being released
     - Summary of changes
     - Note that PR checks will validate version bump and run tests
   - The PR will trigger automated checks (tests, version validation)
   - Once merged, GitHub Actions will automatically publish to PyPI

## Remember:
- Default to patch version bump (0.0.X)
- User can specify "major" or "minor" for different bump types
- Create a release branch, don't commit directly to main
- **IMPORTANT**: Never stop and ask for feedback - execute the full process 