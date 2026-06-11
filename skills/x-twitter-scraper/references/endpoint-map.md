# Endpoint Map

Choose the narrowest route that matches the user request.

## REST

Use REST for bounded, direct calls:

- Tweet lookup and tweet search
- User profile lookup
- User tweets, likes, and media timelines
- Trends
- Media download
- Draw result and giveaway workflows
- Credit balance checks

## Extraction Jobs

Use extraction jobs when the requested result set can be large:

- Followers and following
- Verified followers
- Search result exports
- Replies, quotes, retweets, and favoriters
- User likes and user media
- List and community members
- People search

Always estimate and confirm before creating a job.

## Monitors And Webhooks

Use monitors for ongoing tracking:

- New tweets
- Replies
- Quotes
- Retweets
- Keyword events

Use signed webhooks only when the user provides a destination URL and confirms persistent delivery.

## MCP

Use MCP when an assistant or IDE needs tool access. Route through the public MCP setup docs and keep the same API-key safety rules.

## SDKs

Use SDKs when adding Xquik to application code. Pick the language SDK that matches the target project and keep examples minimal.

## Writes

Use write flows only after explicit approval:

- Create or delete tweets
- Like, unlike, repost, or unrepost
- Follow, unfollow, or remove followers
- Send DMs
- Upload media
- Update profile fields or profile media
- Manage communities

Never retry writes automatically.
