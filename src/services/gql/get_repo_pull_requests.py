# Generated by ariadne-codegen
# Source: ./src/queries/

from typing import Any, List, Literal, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import PullRequestState


class GetRepoPullRequests(BaseModel):
    repository: Optional["GetRepoPullRequestsRepository"]


class GetRepoPullRequestsRepository(BaseModel):
    pull_requests: "GetRepoPullRequestsRepositoryPullRequests" = Field(
        alias="pullRequests"
    )


class GetRepoPullRequestsRepositoryPullRequests(BaseModel):
    page_info: "GetRepoPullRequestsRepositoryPullRequestsPageInfo" = Field(
        alias="pageInfo"
    )
    total_count: int = Field(alias="totalCount")
    nodes: Optional[List[Optional["GetRepoPullRequestsRepositoryPullRequestsNodes"]]]


class GetRepoPullRequestsRepositoryPullRequestsPageInfo(BaseModel):
    has_next_page: bool = Field(alias="hasNextPage")
    end_cursor: Optional[str] = Field(alias="endCursor")


class GetRepoPullRequestsRepositoryPullRequestsNodes(BaseModel):
    merged_at: Optional[Any] = Field(alias="mergedAt")
    title: str
    created_at: Any = Field(alias="createdAt")
    updated_at: Any = Field(alias="updatedAt")
    additions: int
    deletions: int
    commits: "GetRepoPullRequestsRepositoryPullRequestsNodesCommits"
    labels: Optional["GetRepoPullRequestsRepositoryPullRequestsNodesLabels"]
    body: str
    url: Any
    comments: "GetRepoPullRequestsRepositoryPullRequestsNodesComments"
    reviews: Optional["GetRepoPullRequestsRepositoryPullRequestsNodesReviews"]
    merged_by: Optional["GetRepoPullRequestsRepositoryPullRequestsNodesMergedBy"] = (
        Field(alias="mergedBy")
    )
    author: Optional["GetRepoPullRequestsRepositoryPullRequestsNodesAuthor"]
    state: PullRequestState


class GetRepoPullRequestsRepositoryPullRequestsNodesCommits(BaseModel):
    total_count: int = Field(alias="totalCount")


class GetRepoPullRequestsRepositoryPullRequestsNodesLabels(BaseModel):
    edges: Optional[
        List[Optional["GetRepoPullRequestsRepositoryPullRequestsNodesLabelsEdges"]]
    ]


class GetRepoPullRequestsRepositoryPullRequestsNodesLabelsEdges(BaseModel):
    node: Optional["GetRepoPullRequestsRepositoryPullRequestsNodesLabelsEdgesNode"]


class GetRepoPullRequestsRepositoryPullRequestsNodesLabelsEdgesNode(BaseModel):
    name: str


class GetRepoPullRequestsRepositoryPullRequestsNodesComments(BaseModel):
    total_count: int = Field(alias="totalCount")


class GetRepoPullRequestsRepositoryPullRequestsNodesReviews(BaseModel):
    total_count: int = Field(alias="totalCount")


class GetRepoPullRequestsRepositoryPullRequestsNodesMergedBy(BaseModel):
    typename__: Literal[
        "Actor", "Bot", "EnterpriseUserAccount", "Mannequin", "Organization", "User"
    ] = Field(alias="__typename")
    login: str


class GetRepoPullRequestsRepositoryPullRequestsNodesAuthor(BaseModel):
    typename__: Literal[
        "Actor", "Bot", "EnterpriseUserAccount", "Mannequin", "Organization", "User"
    ] = Field(alias="__typename")
    login: str


GetRepoPullRequests.model_rebuild()
GetRepoPullRequestsRepository.model_rebuild()
GetRepoPullRequestsRepositoryPullRequests.model_rebuild()
GetRepoPullRequestsRepositoryPullRequestsNodes.model_rebuild()
GetRepoPullRequestsRepositoryPullRequestsNodesLabels.model_rebuild()
GetRepoPullRequestsRepositoryPullRequestsNodesLabelsEdges.model_rebuild()
