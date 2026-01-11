import os
import glob
import yaml
import json
import datetime
from pathlib import Path

def setup_representer():
    # Configure yaml to handle folded scalars for multiline strings if needed, 
    # but primarily ensuring it dumps readable yaml.
    # Default SafeDumper is usually fine, but we might want to ensure indentation is nice.
    pass

def custom_yaml_dump(data, stream=None):
    return yaml.dump(data, stream, default_flow_style=False, sort_keys=False, allow_unicode=True, width=1000)

def main():
    sources_dir = Path("sources")
    root_dir = Path(".")
    
    compiled_data = {
        "version": 1.0,
        "createdAt": datetime.datetime.now().isoformat(),
        "sources": {}
    }
    
    # Get all yaml files
    yaml_files = sorted(sources_dir.glob("*.yaml"))
    
    print(f"Found {len(yaml_files)} YAML files in {sources_dir}")
    
    for yaml_file in yaml_files:
        try:
            with open(yaml_file, 'r', encoding='utf-8') as f:
                content = yaml.safe_load(f)
                
            if content:
                # Add name derived from filename (without extension)
                source_name = yaml_file.stem
                
                # Use source_name as key
                compiled_data["sources"][source_name] = content
        except Exception as e:
            print(f"Error parsing {yaml_file}: {e}")

    # Write sources.yaml
    output_yaml = root_dir / "sources.yaml"
    with open(output_yaml, 'w', encoding='utf-8') as f:
        custom_yaml_dump(compiled_data, f)
    print(f"Written {output_yaml}")

    # Write sources.json (compressed)
    output_json = root_dir / "sources.json"
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(compiled_data, f, separators=(',', ':'), ensure_ascii=False)
    print(f"Written {output_json}")

if __name__ == "__main__":
    main()
