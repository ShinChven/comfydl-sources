---
name: comfydl-source-manager
description: Manage and create default model source YAML files for the comfydl package. Use when requested to add new models, update existing ones, or organize the sources/ directory.
---

# ComfyDL Source Manager

This skill guides the creation and management of default model sources bundled with `comfydl`.

## Workflow

1.  **Identify Model**: Determine the model name and its download URLs (HuggingFace, Civitai, etc.).
2.  **Create YAML**: Add a new file to `sources/<name>.yaml`.
3.  **Validate**: Ensure the YAML follows the required schema.

## File Structure

All source files MUST be in the `sources/` directory.

## YAML Schema

```yaml
description: "Brief description of the model set"
source: "URL to the model's homepage or documentation (optional)"
downloads:
  - url: "https://huggingface.co/..."
    dest: "models/checkpoints/filename.safetensors"
  - url: "https://civitai.com/api/download/models/ID"
    dest: "models/loras/filename.safetensors"
```

### Constraints
- **Filename**: Short, descriptive, lowercase (e.g., `realvis.yaml`). The filename becomes the `comfydl` subcommand.
- **Destinations**: Use relative paths from the ComfyUI root (e.g., `models/checkpoints/`, `models/loras/`, `models/embeddings/`, `models/vae/`).
- **Civitai Links**: MUST use the API link format `https://civitai.com/api/download/models/ID`. DO NOT include API tokens.
- **Versions**: Create separate files for different model sizes/variants if they are distinct "recipes".

## Testing
No explicit testing command is required for source files.
