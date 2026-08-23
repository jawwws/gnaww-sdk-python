# Gnaww Python SDK

Official Python SDK for the Gnaww print intelligence API.

## Install

```bash
pip install gnaww-sdk
```

## Quick start

```python
import os

from gnaww_sdk import GnawwClient

with GnawwClient(
    api_key=os.environ["GNAWW_API_KEY"],
    workspace_id=os.environ.get("GNAWW_WORKSPACE_ID"),
) as gnaww:
    result = gnaww.consume(
        "500 A5 double-sided flyers on 170gsm silk"
    )
```

Gnaww may return clarification or review requirements when a print requirement is
incomplete. It does not guess unresolved physical attributes.

Capability matching does not by itself confirm price, live availability, producer
acceptance or an order.

Documentation: https://developer.gnaww.io

## Licence

MIT. See `LICENSE`.
