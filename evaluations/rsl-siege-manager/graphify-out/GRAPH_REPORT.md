# Graph Report - .  (2026-05-13)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 833 nodes · 1758 edges · 52 communities (48 shown, 4 thin omitted)
- Extraction: 85% EXTRACTED · 15% INFERRED · 0% AMBIGUOUS · INFERRED: 266 edges (avg confidence: 0.59)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `6085fd66`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]
- [[_COMMUNITY_Community 17|Community 17]]
- [[_COMMUNITY_Community 18|Community 18]]
- [[_COMMUNITY_Community 19|Community 19]]
- [[_COMMUNITY_Community 20|Community 20]]
- [[_COMMUNITY_Community 21|Community 21]]
- [[_COMMUNITY_Community 22|Community 22]]
- [[_COMMUNITY_Community 23|Community 23]]
- [[_COMMUNITY_Community 24|Community 24]]
- [[_COMMUNITY_Community 25|Community 25]]
- [[_COMMUNITY_Community 26|Community 26]]
- [[_COMMUNITY_Community 27|Community 27]]
- [[_COMMUNITY_Community 28|Community 28]]
- [[_COMMUNITY_Community 29|Community 29]]
- [[_COMMUNITY_Community 30|Community 30]]
- [[_COMMUNITY_Community 31|Community 31]]
- [[_COMMUNITY_Community 32|Community 32]]
- [[_COMMUNITY_Community 33|Community 33]]
- [[_COMMUNITY_Community 34|Community 34]]
- [[_COMMUNITY_Community 37|Community 37]]

## God Nodes (most connected - your core abstractions)
1. `SiegeMember` - 55 edges
2. `BoardPage()` - 53 edges
3. `Post Suggestions Modal Handoff` - 40 edges
4. `postsTab` - 29 edges
5. `cn()` - 29 edges
6. `PostsPage()` - 28 edges
7. `BuildingType` - 27 edges
8. `MembersPage()` - 27 edges
9. `MemberRole` - 25 edges
10. `Self-Host on Azure Wiki Page` - 23 edges

## Surprising Connections (you probably didn't know these)
- `A single post assignment suggestion produced by the greedy algorithm.      Attri` --rationale_for--> `PostSuggestionEntry Schema`  [EXTRACTED]
  backend/app/schemas/post_suggestions.py → docs/superpowers/plans/2026-05-09-post-suggestions.md
- `Post Suggestions Modal Handoff` --calls--> `cn()`  [EXTRACTED]
  docs/design-refs/post-suggestions/README.md → frontend/src/lib/utils.ts
- `Discord OAuth2 Authentication Spec` --semantically_similar_to--> `Discord OAuth2 Auth Flow`  [INFERRED] [semantically similar]
  docs/WEB_DESIGN_DOCUMENT.md → CLAUDE.md
- `AuthError` --uses--> `Member`  [INFERRED]
  backend/app/api/auth.py → frontend/src/api/types.ts
- `PostPriorityResponse` --uses--> `PostPriorityConfig`  [INFERRED]
  backend/app/api/post_priority_config.py → frontend/src/api/posts.ts

## Communities (52 total, 4 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.05
Nodes (112): getBoard(), add_group(), generate_images(), Image generation endpoints., Generate PNG images for siege assignments and members list., getNotificationBatch(), notifySiegeMembers(), postToChannel() (+104 more)

### Community 1 - "Community 1"
Cohesion: 0.06
Nodes (67): getMember(), getMemberRoles(), getPostConditions(), updateMemberPreferences(), getSiege(), getSiegeMembers(), getSieges(), MemberRoleInfo (+59 more)

### Community 2 - "Community 2"
Cohesion: 0.05
Nodes (55): API router for the Suggest Post Assignments feature.  Routes:     POST /sieges/{, Generate a greedy post-assignment suggestion preview.      Args:         siege_i, Apply a caller-filtered subset of the stored preview atomically.      Uses SELEC, activateSiege(), applyAttackDay(), applyAutofill(), applyPostSuggestions(), compareSiegesSpecific() (+47 more)

### Community 3 - "Community 3"
Cohesion: 0.05
Nodes (52): asyncpg, FastAPI, OpenTelemetry / Azure Monitor, Playwright (backend dep), PyJWT, Backend Requirements, slowapi, SQLAlchemy (+44 more)

### Community 4 - "Community 4"
Cohesion: 0.06
Nodes (41): PostSuggestionStaleEntry, ChangeCell(), Classification, classify(), ExpiryCountdown, OutcomeFilter, Pill(), PRIORITY_META (+33 more)

### Community 5 - "Community 5"
Cohesion: 0.09
Nodes (45): Application Insights, scripts/bootstrap-images.ps1, Caddy Reverse Proxy, .github/workflows/deploy.yml, Discord OAuth2, GitHub Actions CI/CD, .github/workflows/infra-deploy.yml, Azure Managed Identity (+37 more)

### Community 6 - "Community 6"
Cohesion: 0.06
Nodes (36): health(), createMember(), get_member(), getMemberPreferences(), updateMember(), Send DMs for each member and record results in a fresh DB session., _send_dms(), Find member by username in the guild, open DM, send message. (+28 more)

### Community 7 - "Community 7"
Cohesion: 0.08
Nodes (27): lifespan(), main(), FastAPI application factory and middleware wiring., Run the FastAPI/uvicorn HTTP sidecar on port 8001., Connect and run the Discord client., Start both the Discord client and HTTP server concurrently., Application lifespan — runs startup guards before serving requests., run_discord_client() (+19 more)

### Community 8 - "Community 8"
Cohesion: 0.1
Nodes (17): downgrade(), initial schema  Revision ID: 0001 Revises: Create Date: 2026-03-16, upgrade(), add autofill and attack day preview columns to siege  Revision ID: 0002 Revises:, make siege date nullable  Revision ID: 0003 Revises: 0002 Create Date: 2026-03-1, Add post_priority_config table, Add description to post_priority_config, Replace power with power_level, drop sort_value (+9 more)

### Community 9 - "Community 9"
Cohesion: 0.1
Nodes (24): AuthError, callback(), _check_guild_membership(), _error_redirect(), _exchange_code_for_token(), _get_discord_user(), login(), logout() (+16 more)

### Community 10 - "Community 10"
Cohesion: 0.12
Nodes (17): apiAddBuilding(), apiCreateMember(), apiCreateSiege(), autofillBtn, buildingsTab, chevron, firstPositionSpan, positionCell (+9 more)

### Community 11 - "Community 11"
Cohesion: 0.17
Nodes (14): add_building(), delete_group(), deleteBuilding(), getBuildings(), updateBuilding(), get_team_count(), Return the theoretical total team slots for a building type at a given level., _create_groups_and_positions() (+6 more)

### Community 12 - "Community 12"
Cohesion: 0.16
Nodes (15): VersionInfo, _fetch_bot_version(), getVersion(), Return a version string for the backend.      When both BUILD_NUMBER and GIT_SHA, Call the bot sidecar's /version endpoint. Returns None if unreachable., Return version information for all components., _read_backend_version(), useVersion() (+7 more)

### Community 13 - "Community 13"
Cohesion: 0.13
Nodes (9): BUILDING_LABELS, BuildingColorClass, ActiveTab, BoardPage(), BUILDING_TYPE_ORDER, ROLE_CHIP_COLORS, ROLE_COLORS, ROLE_FILTER_OPTIONS (+1 more)

### Community 14 - "Community 14"
Cohesion: 0.16
Nodes (11): getSiegeMemberPreferences(), DuplicateConditionMap, findPostPosition(), MemberWithMatches, postsTab, priorityBadgeColor(), priorityLabel(), POWER_LABELS (+3 more)

### Community 15 - "Community 15"
Cohesion: 0.19
Nodes (13): build_member_notification_message(), _build_section(), _position_label(), _position_sort_key(), _positions_from_keys(), _positions_to_key_set(), Build rich per-member Discord DM messages for siege assignment notifications., Convert a list of PositionInfo objects to a set of comparable tuples. (+5 more)

### Community 16 - "Community 16"
Cohesion: 0.26
Nodes (12): list_posts(), Build a PostResponse-compatible dict, denormalizing building_number from the rel, _serialize_post(), setPostConditions(), updatePost(), Update a single position's assignment.      Raises:         404 if position not, _validate_member_active(), _get_post_for_siege_or_404() (+4 more)

### Community 17 - "Community 17"
Cohesion: 0.23
Nodes (11): _build_assignments_html(), _build_reserves_html(), generate_assignments_image(), generate_reserves_image(), Image generation service — renders HTML/CSS to PNG via Playwright., Build the reserves/members list HTML string.      Args:         members: Siege m, Render an HTML string to PNG bytes using headless Chromium., Render the assignments board as a PNG. Returns raw PNG bytes. (+3 more)

### Community 18 - "Community 18"
Cohesion: 0.25
Nodes (10): get_changelog_status(), markChangelogSeen(), Changelog status and mark-seen endpoints.  These endpoints let the frontend trac, Raise HTTP 400 if the caller is a service principal.      Args:         current_, Return the authenticated user's last-seen changelog timestamp.      Args:, Set the authenticated user's last-seen changelog timestamp to now.      Idempote, _require_member_session(), ChangelogStatusResponse (+2 more)

### Community 19 - "Community 19"
Cohesion: 0.22
Nodes (5): Carousel(), CarouselProps, CarouselSlide, COLORS, SLIDES

### Community 20 - "Community 20"
Cohesion: 0.24
Nodes (7): AppConfig, fetchConfig(), Layout(), navLinkClass(), RequireAuth(), useAuth(), LandingOrSieges()

### Community 21 - "Community 21"
Cohesion: 0.22
Nodes (7): compareSieges(), ComparisonResult, MemberDiff, PositionKey, _load_assignments(), _load_member_names(), Return {member_id: [PositionKey, ...]} for non-reserve, non-disabled assigned po

### Community 22 - "Community 22"
Cohesion: 0.24
Nodes (9): _get_client_ip(), _parse_retry_after_seconds(), rate_limit_exceeded_handler(), _rate_limit_key(), Rate-limiting utilities shared across the application.  This module owns the sin, Composite key function that honours the AUTH_DISABLED bypass.      When ``AUTH_D, Parse a slowapi rate-limit detail string into a window size in seconds.      slo, Return a JSON 429 response with a ``Retry-After`` header.      Replaces slowapi' (+1 more)

### Community 23 - "Community 23"
Cohesion: 0.22
Nodes (8): DropdownMenuCheckboxItem, DropdownMenuItem, DropdownMenuLabel, DropdownMenuRadioItem, DropdownMenuSeparator, DropdownMenuShortcut(), DropdownMenuSubContent, DropdownMenuSubTrigger

### Community 24 - "Community 24"
Cohesion: 0.22
Nodes (8): Endpoints for Discord guild member ↔ clan member sync., Return proposed Discord ↔ clan member matches without writing to the DB., Apply accepted sync matches, updating discord_username and discord_id., applyDiscordSync(), previewDiscordSync(), Service logic for Discord guild member → clan member matching., Return proposed matches between Discord guild members and clan members.      Mat, Apply accepted sync matches, writing discord_username and discord_id.      Unkno

### Community 25 - "Community 25"
Cohesion: 0.33
Nodes (5): AuthContext, AuthContextValue, AuthProvider(), AuthUser, queryClient

### Community 26 - "Community 26"
Cohesion: 0.4
Nodes (3): ChangelogStatus, fetchChangelogStatus(), DropdownMenuContent

### Community 27 - "Community 27"
Cohesion: 0.33
Nodes (4): apiClient, ERROR_MESSAGES, LoginPage(), MEMBERSHIP_ERRORS

### Community 28 - "Community 28"
Cohesion: 0.33
Nodes (5): get_config(), Public config endpoint — exposes non-sensitive runtime flags to the frontend., Return public runtime configuration flags.      This endpoint is intentionally u, Settings, BaseSettings

### Community 31 - "Community 31"
Cohesion: 0.5
Nodes (3): configure_telemetry(), Application Insights / OpenTelemetry initialisation for the backend.  Call ``con, Initialise Azure Monitor OpenTelemetry and instrument the app.      The ``azure-

### Community 33 - "Community 33"
Cohesion: 0.5
Nodes (3): getPostPriorities(), getPosts(), updatePostPriority()

### Community 34 - "Community 34"
Cohesion: 0.5
Nodes (4): bulk_update_positions(), Apply multiple position updates in a single transaction.      Each update dict m, Validate the logical consistency of position flag combinations., _validate_position_state()

## Ambiguous Edges - Review These
- `bootstrap-images.ps1` → `scripts/bootstrap-images.ps1`  [AMBIGUOUS]
  wiki/Self-Host-on-Azure.md · relation: semantically_similar_to

## Knowledge Gaps
- **259 isolated node(s):** `initial schema  Revision ID: 0001 Revises: Create Date: 2026-03-16`, `add autofill and attack day preview columns to siege  Revision ID: 0002 Revises:`, `make siege date nullable  Revision ID: 0003 Revises: 0002 Create Date: 2026-03-1`, `Add post_priority_config table`, `Add description to post_priority_config` (+254 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `bootstrap-images.ps1` and `scripts/bootstrap-images.ps1`?**
  _Edge tagged AMBIGUOUS (relation: semantically_similar_to) - confidence is low._
- **Why does `Post Suggestions Modal Handoff` connect `Community 4` to `Community 0`, `Community 1`, `Community 2`, `Community 3`, `Community 14`?**
  _High betweenness centrality (0.257) - this node is a cross-community bridge._
- **Why does `Web Design Document` connect `Community 4` to `Community 3`?**
  _High betweenness centrality (0.131) - this node is a cross-community bridge._
- **Are the 13 inferred relationships involving `SiegeMember` (e.g. with `Base` and `Member`) actually correct?**
  _`SiegeMember` has 13 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `Post Suggestions Modal Handoff` (e.g. with `Suggest Post Assignments Feature` and `Post Data Model`) actually correct?**
  _`Post Suggestions Modal Handoff` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `initial schema  Revision ID: 0001 Revises: Create Date: 2026-03-16`, `add autofill and attack day preview columns to siege  Revision ID: 0002 Revises:`, `make siege date nullable  Revision ID: 0003 Revises: 0002 Create Date: 2026-03-1` to the rest of the system?**
  _259 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.05 - nodes in this community are weakly interconnected._