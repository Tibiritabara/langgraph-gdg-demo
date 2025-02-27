"""
Custom types for the tools to harness the data from the GitHub API.
"""

from datetime import datetime

from pydantic import BaseModel, Field

from services.gql.enums import IssueState, PullRequestState, StatusState


class Issues(BaseModel):
    """
    Model to create a dataframe from the issues data.

    Attributes:
        url: The URL of the issue.
        title: The title of the issue.
        state: The state of the issue.
        state_reason: The reason for the state of the issue.
        comments_count: The number of comments on the issue.
        created_at: The date and time the issue was created.
        updated_at: The date and time the issue was last updated.
    """

    url: str
    title: str
    state: IssueState
    state_reason: str | None
    comments_count: int
    created_at: datetime
    updated_at: datetime
    labels: list[str]


class Commits(BaseModel):
    """
    Model to create a dataframe from the commits data.

    Attributes:
        committed_date: The date and time the commit was committed.
        authored_date: The date and time the commit was authored.
        author: The author of the commit.
        message: The message of the commit.
        changed_files_if_available: The number of files changed in the commit.
        additions: The number of additions in the commit.
        deletions: The number of deletions in the commit.
        status: The status of the commit.
    """

    committed_date: datetime
    authored_date: datetime
    author: str | None
    message: str
    changed_files_if_available: int
    additions: int
    deletions: int
    status: StatusState


class PullRequests(BaseModel):
    """
    Model to create a dataframe from the pull requests data.

    Attributes:
        url: The URL of the pull request.
        merged_at: The date and time the pull request was merged.
        title: The title of the pull request.
        created_at: The date and time the pull request was created.
        updated_at: The date and time the pull request was last updated.
        additions: The number of additions in the pull request.
        deletions: The number of deletions in the pull request.
        commits: The number of commits in the pull request.
    """

    url: str
    merged_at: datetime | None
    title: str
    created_at: datetime
    updated_at: datetime
    additions: int
    deletions: int
    commits: int
    reviews: int
    comments: int
    state: PullRequestState
    labels: list[str]


class RepoInput(BaseModel):
    """Input for repository-related tools."""

    owner: str = Field(description="The owner of the repository")
    name: str = Field(description="The name of the repository")
    limit: int = Field(
        description="The number of items to retrieve. The maximum is 50.",
        default=25,
    )


class GetRepoIssuesInput(RepoInput):
    """Input for get_repo_issues tool."""

    states: list[IssueState] = Field(
        description=(
            "Filter issues by state (OPEN, CLOSED). "
            "If not provided, returns all issues."
        ),
    )
    limit: int = Field(
        description="The number of items to retrieve. The maximum is 50.",
        default=25,
    )


class GetRepoPullRequestsInput(RepoInput):
    """Input for get_repo_pull_requests tool."""

    states: list[PullRequestState] = Field(
        description=(
            "Filter pull requests by state (OPEN, CLOSED, MERGED). "
            "If not provided, returns all PRs."
        ),
    )
    limit: int = Field(
        description="The number of items to retrieve. The maximum is 50.",
        default=25,
    )
