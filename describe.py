# /// script
# requires-python = ">=3.11,<3.14"
# dependencies = [
#     "pyyaml",
#     "zai-sdk",
#     "python-dotenv",
#     "sniffio",
#     "tenacity",
# ]
# ///

import os
import yaml
from dataclasses import dataclass
from dotenv import load_dotenv
from pathlib import Path
from typing import Optional
from zai import ZhipuAiClient
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

@dataclass
class PostMetadata:
    date: str
    tags: list[str]
    description: Optional[str] = None

load_dotenv()

client = ZhipuAiClient(api_key=os.getenv("ZAI_API_KEY"))
prompt = '你讲扮演一位资深 SEO 优化专家, 接下来你将会收到一段博客文章的原始 markdown 内容, 请你根据文章内容生成一段 60 字左右的 description 元信息, 你需要直接输出 description 的内容, 不要有任何其余的内容.'

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(Exception)
)
def generate_description(content: str) -> str:
    response = client.chat.completions.create(
        model="GLM-4.5-Flash",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": content},
        ],
    )
    return response.choices[0].message.content.strip()

posts: list[tuple[PostMetadata, str, Path]] = [] # meta, content, path
for path in Path("posts").glob("*.md"):
    content = path.read_text(encoding="utf-8")
    if content.startswith("---"):
        raw_meta = content.split("---", 2)[1].strip()
        data = yaml.safe_load(raw_meta) or {}
        meta = PostMetadata(**{k: v for k, v in data.items() if k in PostMetadata.__annotations__})
        posts.append((meta, content, path))

for meta, content, path in posts:
    if meta.description: continue
    print(f"Generating description for {path.name}...")
    
    meta.description = generate_description(content)
    meta.description = meta.description.replace('\n', ' ')
    meta.description = meta.description.replace('，', ', ')
    meta.description = meta.description.replace('。', '.')
    meta.description = meta.description.replace('：', ': ')

    # 写回文件
    body = content.split("---", 2)[2] if content.count("---") >= 2 else content
    yaml_lines = ["---", f"date: {meta.date}", "tags:"]
    for tag in meta.tags:
        yaml_lines.append(f"  - {tag}")
    yaml_lines.append(f"description: {meta.description}")
    yaml_lines.append("---")
    
    new_content = "\n".join(yaml_lines) + body
    path.write_text(new_content, encoding="utf-8")

print('All done.')
