# ComfyDL Sources

This repository serves as the central source of truth for model definitions used by **comfydl**.

## Live Data Access

The compiled source files are automatically generated and hosted via GitHub Pages:

- **JSON (Compressed / API)**:  
  [https://shinchven.github.io/comfydl-sources/sources.json](https://shinchven.github.io/comfydl-sources/sources.json)

- **YAML (Human Readable)**:  
  [https://shinchven.github.io/comfydl-sources/sources.yaml](https://shinchven.github.io/comfydl-sources/sources.yaml)

## Data Structure

The compiled file follows this schema:

```yaml
version: 1.0
createdAt: "ISO-8601 Timestamp"
sources:
  model_name:                       # Key derived from filename
    description: "Model description"
    source: "https://..."           # Optional: Source URL (e.g., Civitai/HuggingFace)
    downloads:
      - url: "https://..."          # Direct download URL
        dest: "models/..."          # Destination path in ComfyUI
```

### JSON Structure

```json
{
  "version": 1.0,
  "createdAt": "ISO-8601 Timestamp",
  "sources": {
    "model_name": {
      "description": "Model description",
      "source": "https://...",
      "downloads": [
        {
          "url": "https://...",
          "dest": "models/..."
        }
      ]
    }
  }
}
```

## Contributing

To add a new model source:

> **Tip**: When asking an AI assistant to create a new source file, reference `@[MODEL_SOURCE.md]` to provide it with the correct format and guidelines.

1.  Create a new `.yaml` file in the `sources/` directory.
2.  Define the model metadata and download links (see existing files for examples).
    *   The `name` key in the compiled file is derived automatically from the filename.
3.  Commit and push to `main`.

### Automation

A GitHub Action is configured to:
1.  Trigger on push to `main`.
2.  Run `compile_sources.py` to aggregate all YAML files.
3.  Deploy the generated `sources.json` and `sources.yaml` to the `gh-pages` branch.
