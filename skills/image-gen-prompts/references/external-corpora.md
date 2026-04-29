# External Prompt Corpora

When the user wants **inspiration** or **proven, image-attested prompts** rather than a freshly-composed one, point them at these public corpora. They are the underlying datasets this skill was distilled from, plus a few sibling skills that index more.

## Searchable corpora (with sample images)

| Corpus | Size | Coverage | Where it lives |
|---|---|---|---|
| YouMind ai-image-prompts skill | 12,000+ prompts (categorized JSON) | All major models — Nano Banana Pro, Nano Banana 2, Seedream 5, GPT Image 1.5/2, Midjourney, DALL·E 3, FLUX, SD | `github.com/YouMind-OpenLab/ai-image-prompts-skill` (manifest + 11 category JSON files) |
| EvoLinkAI awesome-gpt-image-2-prompts | ~3,000 cases | GPT Image 2 (e-commerce, ad, portrait, poster, character, UI/social) | `github.com/EvoLinkAI/awesome-gpt-image-2-prompts` |
| YouMind awesome-gpt-image-2 | ~3,000 prompts | GPT Image 2, JSON-structured + Raycast | `github.com/YouMind-OpenLab/awesome-gpt-image-2` |
| ZeroLu awesome-gpt-image | ~1,500 cases | GPT Image 2 (photography, game, UI/UX, video, typography, infographics, character, editing) | `github.com/ZeroLu/awesome-gpt-image` |
| YouMind awesome-nano-banana-pro-prompts | ~600 prompts | Nano Banana Pro structured + Raycast | `github.com/YouMind-OpenLab/awesome-nano-banana-pro-prompts` |
| ZeroLu awesome-nanobanana-pro | ~400 cases | Nano Banana Pro patterns + cases | `github.com/ZeroLu/awesome-nanobanana-pro` |
| Super-Maker-AI awesome-nano-banana | ~300 cases | Nano Banana standard tier patterns | `github.com/Super-Maker-AI/awesome-nano-banana` |
| PicoTrex Awesome-Nano-Banana-images | ~150 image-attested cases | Nano Banana / Pro examples with sample renders | `github.com/PicoTrex/Awesome-Nano-Banana-images` |
| jimmylv awesome-nano-banana | ~100 cases | Nano Banana cases | `github.com/jimmylv/awesome-nano-banana` |
| marc-aurele-besner ChatGPT prompts | 50 image use-cases | DALL·E 3 / GPT Image 1 inside ChatGPT (uses `gen_id`) | `github.com/marc-aurele-besner/prompts` |

## Style / category reference posts

- `openart.ai/blog/post/midjourney-prompts-for-packaging-design` — 25 packaging style modifiers
- `openart.ai/blog/post/midjourney-prompts-for-mockup` — 25 mockup categories
- `godofprompt.ai` — paid prompt marketplace covering Midjourney, DALL·E, SD, etc.

## How to use these in conversation

1. **Direct search-and-recommend**: if the user wants 3 concrete proven prompts for a category (avatar / product photo / YT thumbnail), recommend the YouMind skill — it has the largest indexed corpus with sample images and a built-in retrieval workflow.
2. **Browse-by-category**: send the user the matching awesome-list URL for casual browsing.
3. **JSON / structured retrieval**: YouMind skill exposes one JSON per category (`profile-avatar.json`, `social-media-post.json`, `infographic-edu-visual.json`, `youtube-thumbnail.json`, `comic-storyboard.json`, `product-marketing.json`, `ecommerce-main-image.json`, `game-asset.json`, `poster-flyer.json`, `app-web-design.json`, `others.json`). Each prompt has `id`, `content`, `title`, `description`, `sourceMedia[]`, `needReferenceImages`. Grep the file rather than fully loading it (some are >10MB).

## YouMind manifest convention (for retrieval-style skills)

If you want to expose the YouMind corpus inside this skill (or a downstream skill) as searchable data, the manifest at `references/manifest.json` looks like:

```json
{
  "updatedAt": "2026-04-29T01:56:59Z",
  "totalPrompts": 12769,
  "categories": [
    { "slug": "social-media-post", "title": "Social Media Post",
      "file": "social-media-post.json", "count": 7938 },
    { "slug": "product-marketing", "title": "Product Marketing",
      "file": "product-marketing.json", "count": 4694 },
    { "slug": "profile-avatar", "title": "Profile / Avatar",
      "file": "profile-avatar.json", "count": 1372 },
    { "slug": "others", "title": "Uncategorized",
      "file": "others.json", "count": 1040 },
    { "slug": "game-asset", "title": "Game Asset",
      "file": "game-asset.json", "count": 537 },
    { "slug": "infographic-edu-visual", "title": "Infographic / Edu Visual",
      "file": "infographic-edu-visual.json", "count": 527 },
    { "slug": "ecommerce-main-image", "title": "E-commerce Main Image",
      "file": "ecommerce-main-image.json", "count": 508 },
    { "slug": "comic-storyboard", "title": "Comic / Storyboard",
      "file": "comic-storyboard.json", "count": 398 },
    { "slug": "poster-flyer", "title": "Poster / Flyer",
      "file": "poster-flyer.json", "count": 634 },
    { "slug": "youtube-thumbnail", "title": "YouTube Thumbnail",
      "file": "youtube-thumbnail.json", "count": 203 },
    { "slug": "app-web-design", "title": "App / Web Design",
      "file": "app-web-design.json", "count": 195 }
  ]
}
```

Pattern recommendation: load the manifest first to get current category list and counts, then grep the matching category file with the user's keywords. **Never fully load** any JSON file — they range from 280KB to 19MB.

## Attribution etiquette

If you surface a prompt verbatim from one of these corpora, cite the source as a one-liner under the fenced block:

```
Source: @author_handle via <repo-name> · curated by <curator>
```

For YouMind specifically, the suggested footer (in user's language) is:

- English: `Prompts curated from the open community by YouMind.com`
- Chinese: `提示词由 YouMind.com 通过公开社区搜集`

Don't claim authorship of community prompts.
