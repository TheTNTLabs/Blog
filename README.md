# TheTNTLabs Blog

[![status-badge](https://ci.codeberg.org/api/badges/TheTNTLabs/Blog/status.svg)](https://ci.codeberg.org/TheTNTLabs/Blog)
[![license-badge](https://img.shields.io/badge/license-CC--BY--4.0_&_MIT-blue)](https://codeberg.org/TheTNTLabs/Blog/src/branch/main/LICENSE.md)
[![chat-badge](https://img.shields.io/badge/chat-on_Zulip-blue)](https://thetntlabs.zulipchat.com/)
[![github-mirror-badge](https://img.shields.io/badge/mirrored-to_GitHub-black)](https://github.com/TheTNTLabs/Blog)
[![gitlab-mirror-badge](https://img.shields.io/badge/mirrored-to_GitLab-orange)](https://gitlab.com/TheTNTLabs/Blog)

## Setup

### 1. Install Pelican and Markdown
```bash
python3 -m pip install "pelican[markdown]"
```

### 2. Generate the site
```bash
pelican content
```

### 3. Preview the site
```bash
pelican --listen
```
