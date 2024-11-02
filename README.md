# TheTNTLabs Blog

[![status-badge](https://ci.codeberg.org/api/badges/TheTNTLabs/Blog/status.svg)](https://ci.codeberg.org/TheTNTLabs/Blog)
[![license-badge](https://img.shields.io/badge/license-CC--BY--4.0_&_MIT-blue)](https://codeberg.org/TheTNTLabs/Blog/src/branch/main/LICENSE.md)
[![chat-badge](https://img.shields.io/badge/chat-on_Zulip-blue)](https://thetntlabs.zulipchat.com/)

## 1. Install Python packages
`python3 -m pip install "pelican[markdown]"`

## 2. Generate static files
`pelican content`

## 3. Serve generated files locally
`python3 -m http.server -d static-deployment/`
