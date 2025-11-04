# Branch Protection Setup

This document explains how to configure branch protection for the `main` branch to enforce PR-based workflows with automated validation.

## GitHub Settings Configuration

You **must** configure these settings on GitHub (they cannot be done in code):

### 1. Navigate to Branch Protection Settings

1. Go to your repository on GitHub
2. Click **Settings** → **Branches**
3. Under "Branch protection rules", click **Add rule**
4. In "Branch name pattern", enter: `main`

### 2. Required Protection Settings

Enable the following options:

#### ✅ Require a pull request before merging
- **Required approvals**: 0 (for solo projects) or 1+ (for team projects)
- ✅ **Dismiss stale pull request approvals when new commits are pushed** (recommended)
- ✅ **Require approval of the most recent reviewable push** (recommended)

#### ✅ Require status checks to pass before merging
- ✅ **Require branches to be up to date before merging**
- Add these required status checks:
  - `test` - Ensures all tests pass
  - `version-check` - Ensures version is bumped (for code changes)
  - `pr-status` - Overall PR validation status

#### ✅ Require conversation resolution before merging (optional but recommended)

#### ✅ Do not allow bypassing the above settings (recommended)
- This prevents even admins from pushing directly to main

### 3. Save Changes

Click **Create** or **Save changes** at the bottom.

## What This Protects Against

With these settings enabled:

- ❌ **Cannot push directly to main** - All changes must go through a PR
- ❌ **Cannot merge PRs with failing tests** - Tests must pass
- ❌ **Cannot merge PRs without version bump** - Version must be incremented for code changes
- ✅ **Documentation/README changes** can merge without version bumps
- ✅ **All changes are reviewed and validated** before reaching main

## Workflow Overview

### For Code Changes (requires version bump):

1. Create a feature branch: `git checkout -b feature/my-feature`
2. Make your changes
3. Bump version in `pyproject.toml` (use `/publish` command)
4. Push and create PR: `gh pr create`
5. Automated checks run:
   - Tests
   - Version bump validation
   - PyPI version conflict check
6. Merge PR when checks pass
7. GitHub Actions automatically publishes to PyPI

### For Documentation Changes (no version bump needed):

1. Create a docs branch: `git checkout -b docs/update-readme`
2. Make your changes (only to `docs/`, `README.md`, `.github/workflows/`)
3. Push and create PR: `gh pr create`
4. Automated checks run:
   - Tests (always required)
   - Version check is skipped for docs-only changes
5. Merge PR when checks pass
6. No PyPI publish (docs-only changes don't trigger publish)

## Automated Workflows

### `.github/workflows/pr-checks.yml`

Runs on every PR to `main`:

- **Test Job**: Runs all tests (always required)
- **Version Check Job**: Validates version bump (only for code changes)
- **Status Job**: Ensures all required checks passed

### `.github/workflows/publish.yml`

Runs when PRs are merged to `main`:

- Only triggers for code changes (ignores docs/README/workflow changes)
- Builds the package
- Publishes to PyPI using trusted publishing

## Testing the Setup

After configuring branch protection:

1. **Test direct push rejection**:
   ```bash
   git checkout main
   echo "test" >> test.txt
   git add test.txt
   git commit -m "Test direct push"
   git push
   ```
   **Expected**: Push should be rejected with an error about branch protection.

2. **Test PR without version bump**:
   ```bash
   git checkout -b test-branch
   echo "test" >> src/macscribe/cli.py
   git add src/macscribe/cli.py
   git commit -m "Test change"
   git push -u origin test-branch
   gh pr create
   ```
   **Expected**: PR checks should fail with "Version not bumped" error.

3. **Test docs-only PR**:
   ```bash
   git checkout -b test-docs
   echo "# Update" >> README.md
   git add README.md
   git commit -m "Update README"
   git push -u origin test-docs
   gh pr create
   ```
   **Expected**: PR checks should pass (version bump not required for docs).

## Troubleshooting

### "Version check failed" but I only changed docs

Make sure you only modified files in:
- `docs/**`
- `README.md`
- `.github/workflows/**`

If you modified any code files, you must bump the version.

### "Tests failed" on PR

1. Run tests locally: `uv run pytest tests/ -v`
2. Fix failing tests
3. Push the fixes - PR will automatically re-run checks

### "Status check not found"

The status checks won't appear until you create your first PR. After the first PR, they'll be available to add as required checks in branch protection settings.

### Need to bypass branch protection temporarily

If you're an admin and need to bypass (use sparingly):
1. Go to Settings → Branches
2. Edit the branch protection rule
3. Check "Allow specified actors to bypass required pull requests"
4. Add yourself
5. Make your change
6. Remove the bypass permission

Or better: Create a PR even for urgent changes to maintain audit trail.

## Benefits

- ✅ **Quality control**: All changes reviewed and tested
- ✅ **Version management**: Automatic validation of version bumps
- ✅ **CI/CD**: Automated publishing on merge
- ✅ **Audit trail**: All changes tracked via PRs
- ✅ **Collaboration**: Easy to review and discuss changes
- ✅ **Rollback**: Simple to revert via PR history
